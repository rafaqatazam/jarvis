from typing import List
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import DuckDuckGoSearchRun, WikipediaQueryRun
from langchain.chains import LLMMathChain
from langchain.agents import Tool
from .constants import ToolConfig

class ToolFactory:
    
    @staticmethod
    def create_wikipedia_tool() -> WikipediaQueryRun:
        config = ToolConfig.WIKIPEDIA_TOOL.value
        api_wrapper = WikipediaAPIWrapper(top_k_results=config["top_results"], doc_content_chars_max=config["max_character"])
        return WikipediaQueryRun(api_wrapper=api_wrapper)

    @staticmethod
    def create_duck_duck_go_tool() -> DuckDuckGoSearchRun:
        return DuckDuckGoSearchRun()

    @staticmethod
    def create_math_tool(llm) -> Tool:
        llm_math_chain = LLMMathChain.from_llm(llm=llm)
        config = ToolConfig.MATH_TOOL.value
        return Tool.from_function(
            func=llm_math_chain.run,
            name=config["name"],
            description=config["description"]
        )

    @staticmethod
    def create_tools(llm) -> List[Tool]:
        tools = [
            ToolFactory.create_wikipedia_tool(),
            ToolFactory.create_duck_duck_go_tool(),
            ToolFactory.create_math_tool(llm)
        ]
        return tools
