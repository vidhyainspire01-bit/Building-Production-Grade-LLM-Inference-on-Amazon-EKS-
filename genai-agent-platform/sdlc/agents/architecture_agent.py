from shared.base_agent import BaseAgent

class ArchitectureAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            system_prompt="Design architecture diagrams, modules, contracts and flows."
        )
