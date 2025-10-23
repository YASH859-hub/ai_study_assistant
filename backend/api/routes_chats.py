from fastapi import APIRouter
from core.rag_pipeline import query_rag

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("/")
async def chat(query: dict):
    question = query.get("question")
    answer = query_rag(question)
    return {"answer": answer}
