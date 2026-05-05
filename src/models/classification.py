# from typing import Any
# from pydantic import BaseModel, Field


# class ExtractedEntities(BaseModel):
#     tickers: list[str] = Field(default_factory=list)
#     topics: list[str] = Field(default_factory=list)
#     sectors: list[str] = Field(default_factory=list)
#     amount: float | None = None
#     rate: float | None = None
#     period_years: int | None = None
#     currency: str | None = None
#     index: str | None = None
#     action: str | None = None
#     goal: str | None = None
#     frequency: str | None = None
#     horizon: str | None = None
#     time_period: str | None = None
#     raw: dict[str, Any] = Field(default_factory=dict)


# class ClassificationResult(BaseModel):
#     intent: str
#     target_agent: str
#     extracted_entities: ExtractedEntities = Field(default_factory=ExtractedEntities)
#     safety_verdict: str = "safe"
#     confidence: float | None = None


from typing import Any
from pydantic import BaseModel, Field


class ExtractedEntities(BaseModel):
    tickers: list[str] = Field(default_factory=list)
    topics: list[str] = Field(default_factory=list)
    sectors: list[str] = Field(default_factory=list)
    amount: float | None = None
    rate: float | None = None
    period_years: int | None = None
    currency: str | None = None
    index: str | None = None
    action: str | None = None
    goal: str | None = None
    frequency: str | None = None
    horizon: str | None = None
    time_period: str | None = None
    raw: dict[str, Any] = Field(default_factory=dict)


class ClassificationResult(BaseModel):
    intent: str
    target_agent: str
    extracted_entities: ExtractedEntities = Field(default_factory=ExtractedEntities)
    safety_verdict: str = "safe"
    confidence: float | None = None

    @property
    def agent(self) -> str:
        return self.target_agent

    @property
    def entities(self) -> dict[str, Any]:
        return self.extracted_entities.model_dump(exclude_none=True)