import logging
from .agent_service import AgentService

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Bot:
    def __init__(self, model_type: str, agent_type: str = 'react'):
        self.agent_service = AgentService(model_type, agent_type)

    def ask(self, user_prompt: str) -> str:
        try:
            agent_executor = self.agent_service.create_agent()
            response = agent_executor.invoke({"input": user_prompt})
            formatted_response = f'Prompt: {response["input"]}\nResponse: {response["output"]}\n{"="*50}'
            logging.info(formatted_response)
            return response['output']
        except Exception as e:
            logging.error(f'An error occurred: {e}')
            raise
