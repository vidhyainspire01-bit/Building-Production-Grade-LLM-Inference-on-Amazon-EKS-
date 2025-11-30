from shared.base_agent import BaseAgent

class SignalUnifierAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            system_prompt=(
                "You are a Signal Unifier. Merge Slack, CRM, Calls, Support"
                " into a single normalized customer timeline."
            )
        )
