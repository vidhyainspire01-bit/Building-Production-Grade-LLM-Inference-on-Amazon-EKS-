from shared.base_agent import BaseAgent

class CodeGenAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            system_prompt="Generate Python/Node/Infra code based on architecture."
        )
