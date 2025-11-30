from typing import Dict, Any
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

class BaseAgent:
    def __init__(self, system_prompt: str, model="gpt-4o-mini"):
        self.llm = ChatOpenAI(model=model)
        self.system_prompt = system_prompt

    async def run(self, input: str) -> Dict[str, Any]:
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": input},
        ]
        response = await self.llm.ainvoke(messages)
        return {"agent_response": response.content}
