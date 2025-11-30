# src/api/routes/llm.py

from fastapi import APIRouter
from src.schemas.llm_request import LLMRequest
from src.core.router import LLMRouter

router = APIRouter()
llm_router = LLMRouter()

@router.post("/invoke")
async def invoke_llm(request: LLMRequest):
    response = await llm_router.dispatch(request)
    return response
