from typing import Union
from decouple import config
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from .constants import ANTHROPIC_MODEL

class LLMFactory:
    
    @staticmethod
    def create_llm(model_type: str) -> Union[ChatOpenAI, ChatAnthropic]:
        if model_type == 'anthropic':
            return ChatAnthropic(api_key=config('ANTHROPIC_API_KEY'), model=ANTHROPIC_MODEL)
        elif model_type == 'openai':
            return ChatOpenAI(openai_api_key=config('OPENAI_KEY'))
        else:
            raise ValueError("Invalid model type specified.")
