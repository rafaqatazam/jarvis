from enum import Enum

class AgentTypes(Enum):
    REACT = 'react'
    OPENAI_FUNCTIONS = 'openai_functions'

class ToolNames(Enum):
    MATH = "Calculator"
    WIKIPEDIA = "Wikipedia Query"
    DUCK_DUCK_GO = "DuckDuckGo Search"

class ToolConfig(Enum):
    MATH_TOOL = {
        "name": ToolNames.MATH.value,
        "description": (
            "Useful for when you need to answer questions about math. "
            "This tool is only for math questions and nothing else. Only input math expressions."
        )
    }
    WIKIPEDIA_TOOL = {
        "name": ToolNames.WIKIPEDIA.value,
        "top_results": 2,
        "max_character": 200,
    }
    DUCK_DUCK_GO_TOOL = {
        "name": ToolNames.DUCK_DUCK_GO.value,
    }

ANTHROPIC_MODEL = 'claude-3-sonnet-20240229'