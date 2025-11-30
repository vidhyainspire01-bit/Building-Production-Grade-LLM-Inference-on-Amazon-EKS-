from shared.base_agent import BaseAgent

class RequirementAnalyzer(BaseAgent):
    def __init__(self):
        super().__init__(
            system_prompt="Analyze user stories, extract acceptance criteria and dependencies."
        )
