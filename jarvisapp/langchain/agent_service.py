from langchain import hub
from langchain.agents import create_react_agent, create_openai_functions_agent, AgentExecutor
from .llm_factory import LLMFactory
from .tool_factory import ToolFactory
from .constants import AgentTypes

class AgentService:
    def __init__(self, model_type: str, agent_type: str = AgentTypes.REACT.value):
        self.llm = LLMFactory.create_llm(model_type)
        self.agent_type = agent_type

    def create_agent(self) -> AgentExecutor:
        tools = ToolFactory.create_tools(self.llm)
        prompt = self._get_prompt()

        if self.agent_type == AgentTypes.REACT.value:
            agent = create_react_agent(self.llm, tools, prompt)
        elif self.agent_type == AgentTypes.OPENAI_FUNCTIONS.value:
            agent = create_openai_functions_agent(self.llm, tools, prompt)
        else:
            raise ValueError(f"Invalid agent type specified: {self.agent_type}. Please choose '{AgentTypes.REACT.value}' or '{AgentTypes.OPENAI_FUNCTIONS.value}'.")

        return AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)

    def _get_prompt(self) -> str:
        if self.agent_type == AgentTypes.REACT.value:
            return hub.pull("hwchase17/react")
        elif self.agent_type == AgentTypes.OPENAI_FUNCTIONS.value:
            return hub.pull("hwchase17/openai-functions-agent")
        else:
            raise ValueError(f"Invalid agent type specified: {self.agent_type}. Please choose '{AgentTypes.REACT.value}' or '{AgentTypes.OPENAI_FUNCTIONS.value}'.")
