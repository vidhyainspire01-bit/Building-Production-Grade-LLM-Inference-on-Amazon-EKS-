from shared.base_agent import BaseAgent

class SummarizerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            system_prompt=(
                "Generate an executive summary with priorities, risks, "
                "and actions. Use short, crisp language."
            )
        )
