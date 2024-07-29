# from langchain_anthropic import ChatAnthropic
# from langchain_openai import ChatOpenAI
# from langchain_core.tools import Tool
# from langchain.agents import ZeroShotAgent, Tool, AgentExecutor

# from langchain_core.output_parsers import StrOutputParser

from decouple import config

# from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate, PromptTemplate

from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import create_openai_functions_agent, AgentExecutor
# from langchain.schema import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

from langchain.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

from langchain.tools import DuckDuckGoSearchRun

from langchain.chains import LLMMathChain
from langchain.agents import Tool


def askBot(user_prompt):
    print('Prompt: ' + user_prompt)
    SECRET_KEY = config('OPENAI_KEY')
    # openai_llm = ChatOpenAI(openai_api_key=SECRET_KEY)
    llm = ChatOpenAI(openai_api_key=SECRET_KEY)

    prompt = hub.pull("hwchase17/openai-functions-agent")
    print(prompt)
    
    ## Wikipedia api wrapper
    api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
    api_wrapper_tool = WikipediaQueryRun(api_wrapper=api_wrapper)
    
    ## DuckDuckGo wrapper
    # searchDuckDuck = DuckDuckGoSearchRun()

    ## LLM Math
    llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)
    math_tool = Tool.from_function(
        func=llm_math_chain.run,
        name="Calculator",
        description="Useful for when you need to answer questions about math. This tool is only for math questions and nothing else. Only input math expressions.",
    )

    # tools = [api_wrapper_tool, searchDuckDuck, math_tool]
    tools = [api_wrapper_tool, math_tool]

    agent = create_openai_functions_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools)

    response = agent_executor.invoke({"input": user_prompt})

    print('**********************')
    print(response)
    print('**********************')

    print('Prompt: ' + response['input'] + '\n Response: ' + response['output'] + '===================================================')
    return response['output']

    