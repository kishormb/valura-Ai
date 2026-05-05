# from typing import Any, Literal
# from pydantic import BaseModel, Field


# class SafetyResult(BaseModel):
#     allowed: bool
#     category: str | None = None
#     message: str | None = None


# class Observation(BaseModel):
#     severity: Literal["info", "warning", "critical"]
#     text: str


# class ConcentrationRisk(BaseModel):
#     top_position_pct: float | None = None
#     top_3_positions_pct: float | None = None
#     flag: str


# class PerformanceMetrics(BaseModel):
#     total_return_pct: float | None = None
#     annualized_return_pct: float | None = None


# class BenchmarkComparison(BaseModel):
#     benchmark: str
#     portfolio_return_pct: float | None = None
#     benchmark_return_pct: float | None = None
#     alpha_pct: float | None = None


# class PortfolioHealthResponse(BaseModel):
#     status: str = "ok"
#     concentration_risk: ConcentrationRisk
#     performance: PerformanceMetrics
#     benchmark_comparison: BenchmarkComparison | None = None
#     observations: list[Observation] = Field(default_factory=list)
#     disclaimer: str
#     metadata: dict[str, Any] = Field(default_factory=dict)


# class StubAgentResponse(BaseModel):
#     status: str = "not_implemented"
#     intent: str
#     agent: str
#     entities: dict[str, Any]
#     message: str


# class ErrorPayload(BaseModel):
#     code: str
#     message: str



from typing import Any, Literal
from pydantic import BaseModel, Field


class SafetyResult(BaseModel):
    allowed: bool
    category: str | None = None
    message: str | None = None

    @property
    def blocked(self) -> bool:
        return not self.allowed


class Observation(BaseModel):
    severity: Literal["info", "warning", "critical"]
    text: str


class ConcentrationRisk(BaseModel):
    top_position_pct: float | None = None
    top_3_positions_pct: float | None = None
    flag: str


class PerformanceMetrics(BaseModel):
    total_return_pct: float | None = None
    annualized_return_pct: float | None = None


class BenchmarkComparison(BaseModel):
    benchmark: str
    portfolio_return_pct: float | None = None
    benchmark_return_pct: float | None = None
    alpha_pct: float | None = None


class PortfolioHealthResponse(BaseModel):
    status: str = "ok"
    concentration_risk: ConcentrationRisk
    performance: PerformanceMetrics
    benchmark_comparison: BenchmarkComparison | None = None
    observations: list[Observation] = Field(default_factory=list)
    disclaimer: str
    metadata: dict[str, Any] = Field(default_factory=dict)


class StubAgentResponse(BaseModel):
    status: str = "not_implemented"
    intent: str
    agent: str
    entities: dict[str, Any]
    message: str