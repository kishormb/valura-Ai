from pydantic import BaseModel, Field


class QueryRequest(BaseModel):
    session_id: str = Field(min_length=1)
    user_id: str = Field(min_length=1)
    query: str = Field(min_length=1)