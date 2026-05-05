from fastapi import APIRouter, Depends
from sse_starlette.sse import EventSourceResponse

from src.dependencies import get_orchestrator
from src.models.requests import QueryRequest

router = APIRouter()


@router.post("/query")
async def query_endpoint(request: QueryRequest, orchestrator=Depends(get_orchestrator)):
    return EventSourceResponse(
        orchestrator.stream(
            session_id=request.session_id,
            user_id=request.user_id,
            query=request.query,
        )
    )