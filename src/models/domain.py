# from __future__ import annotations

# from typing import Any
# from pydantic import BaseModel, Field


# class Holding(BaseModel):
#     ticker: str
#     quantity: float = 0.0
#     avg_cost: float | None = None
#     currency: str | None = None
#     market: str | None = None
#     sector: str | None = None
#     weight_pct: float | None = None
#     metadata: dict[str, Any] = Field(default_factory=dict)


# class UserProfile(BaseModel):
#     user_id: str
#     name: str | None = None
#     country: str | None = None
#     base_currency: str | None = None
#     risk_profile: str | None = None
#     kyc_status: str | None = None
#     investment_objective: str | None = None
#     holdings: list[Holding] = Field(default_factory=list)
#     metadata: dict[str, Any] = Field(default_factory=dict)


from __future__ import annotations

from typing import Any
from pydantic import BaseModel, Field


class Holding(BaseModel):
    ticker: str
    quantity: float = 0.0
    avg_cost: float | None = None
    currency: str | None = None
    market: str | None = None
    sector: str | None = None
    weight_pct: float | None = None
    purchased_at: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)


class UserProfile(BaseModel):
    user_id: str
    name: str | None = None
    age: int | None = None
    country: str | None = None
    base_currency: str | None = None
    risk_profile: str | None = None
    kyc_status: str | None = None
    investment_objective: str | None = None
    holdings: list[Holding] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)