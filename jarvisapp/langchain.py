from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser

from decouple import config

from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
# from langchain_openai import ChatOpenAI
# from decouple import config

# def askJarvis(user_prompt, model_type):
#     SECRET_KEY = config('OPENAI_KEY')
#     chat = ChatOpenAI(openai_api_key=SECRET_KEY)
#     SystemMessagePrompt = SystemMessagePromptTemplate.from_template("Your name is Jarvis. You are a master chef and you just want to reply to recipe queries only.")
#     HumanMessagePrompt = HumanMessagePromptTemplate.from_template('{asked_recipe}')

#     chatPrompt = ChatPromptTemplate.from_messages([
#         SystemMessagePrompt,
#         HumanMessagePrompt
#     ])

#     formattedChatPrompt = chatPrompt.format_messages(asked_recipe=user_prompt)
#     # print(formattedChatPrompt)
#     response = chat.invoke(formattedChatPrompt)
#     # print(' got tyhe response form OPENAI \n\n')
#     # print('Response: ' + response.content)
#     # print('\n\n')
#     return response.content

def askJarvis(user_prompt, model_type):
    if model_type == 'openai':
        SECRET_KEY = config('OPENAI_KEY')
        chat = ChatOpenAI(openai_api_key=SECRET_KEY)
        SystemMessagePrompt = SystemMessagePromptTemplate.from_template("Your name is Jarvis. You are a helpful assistant")
        HumanMessagePrompt = HumanMessagePromptTemplate.from_template('{asked_question}')

        chatPrompt = ChatPromptTemplate.from_messages([
            SystemMessagePrompt,
            HumanMessagePrompt
        ])

        formattedChatPrompt = chatPrompt.format_messages(asked_question=user_prompt)
        # print(formattedChatPrompt)
        response = chat.invoke(formattedChatPrompt)
        response_prefix = f"Responded by: {model_type}\n" if model_type else ""
        
        return response_prefix + response.content
    elif model_type == 'llama':
        # llm = ChatOllama(model="llama3")
        # prompt = ChatPromptTemplate.from_template(user_prompt)

        # chain = prompt | llm | StrOutputParser()
        # return chain.invoke({"user_prompt": user_prompt})

        llm = ChatOllama(model="llama3")
        prompt = ChatPromptTemplate.from_template("{topic}")
        chain = prompt | llm | StrOutputParser()
        response_prefix = f"Responded by: {model_type}\n" if model_type else ""
        return response_prefix + chain.invoke({"topic": user_prompt})
    else:
        return "Invalid model selected"