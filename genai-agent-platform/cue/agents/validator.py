from shared.base_agent import BaseAgent

class ValidatorAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            system_prompt=(
                "Validate claims with citations from source events. "
                "Ensure every insight links back to data."
            )
        )
