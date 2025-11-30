from shared.base_agent import BaseAgent

class ReviewerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            system_prompt="Review code for security, quality, performance, and missing tests."
        )
