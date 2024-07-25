
from decouple import config
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain.agents import Tool
from langchain import hub
from langchain.agents import create_react_agent, create_openai_functions_agent, AgentExecutor
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import DuckDuckGoSearchRun, WikipediaQueryRun


# from langchain.tools import DuckDuckGoSearchRun
from langchain.chains import LLMMathChain

def getAllTools(llm):
    ## Wikipedia api wrapper
    api_wrapper = WikipediaAPIWrapper(top_k_results=2, doc_content_chars_max=200)
    api_wrapper_tool = WikipediaQueryRun(api_wrapper=api_wrapper)
    
    ## DuckDuckGo wrapper
    searchDuckDuck = DuckDuckGoSearchRun()

    ## LLM Math
    llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)
    math_tool = Tool.from_function(
        func=llm_math_chain.run,
        name="Calculator",
        description="Useful for when you need to answer questions about math. This tool is only for math questions and nothing else. Only input math expressions.",
    )

    return [api_wrapper_tool, searchDuckDuck, math_tool]

def initLLM(model_type):
    if model_type == 'anthropic':
        SECRET_KEY = config('ANTHROPIC_API_KEY')
        return ChatAnthropic(api_key=SECRET_KEY, model='claude-3-sonnet-20240229')
    elif model_type == 'openai':
        SECRET_KEY = config('OPENAI_KEY')
        return ChatOpenAI(openai_api_key=SECRET_KEY)
    else:
        raise ValueError("Invalid model type specified. Please choose 'anthropic' or 'openai'.")

def askBot(user_prompt):
    print('Prompt: ' + user_prompt)
    
    ## LLM
    # llm = initLLM('anthropic')
    llm = initLLM('openai')

    ## OPENAI Base Prompt
    # prompt = hub.pull("hwchase17/openai-functions-agent")
    prompt = hub.pull("hwchase17/react")
    
    ## Tools
    tools = getAllTools(llm)

    ## Agents
    # agent = create_openai_functions_agent(llm, tools, prompt)
    agent = create_react_agent(llm, tools, prompt)

    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)
    response = agent_executor.invoke({"input": user_prompt})

    print('Prompt: ' + response['input'] + '\n Response: ' + response['output'] + '===================================================')
    return response['output']

    