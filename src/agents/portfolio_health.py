
from src.models.domain import Holding, UserProfile

from src.models.responses import (
    BenchmarkComparison,
    ConcentrationRisk,
    Observation,
    PerformanceMetrics,
    PortfolioHealthResponse,
)

DISCLAIMER = (
    "This is not investment advice. It is an educational portfolio summary "
    "based on the data available and may be incomplete or delayed."
)
def _coerce_user(user) -> UserProfile:
    if isinstance(user, UserProfile):
        return user

    if isinstance(user, dict):
        raw_positions = user.get("positions", [])
        holdings = [
            Holding(
                ticker=pos.get("ticker", "UNKNOWN"),
                quantity=pos.get("quantity", 0.0),
                avg_cost=pos.get("avg_cost"),
                currency=pos.get("currency"),
                market=pos.get("exchange"),
                sector=pos.get("sector"),
                weight_pct=pos.get("weight_pct", pos.get("weight")),
                purchased_at=pos.get("purchased_at"),
                metadata=pos,
            )
            for pos in raw_positions
        ]
        return UserProfile(
            user_id=user.get("user_id", "unknown"),
            name=user.get("name"),
            age=user.get("age"),
            country=user.get("country"),
            base_currency=user.get("base_currency"),
            risk_profile=user.get("risk_profile"),
            kyc_status=(user.get("kyc") or {}).get("status"),
            investment_objective=((user.get("preferences") or {}).get("goal")),
            holdings=holdings,
            metadata=user,
        )

    raise TypeError("Unsupported user type")

class PortfolioHealthAgent:
    def __init__(self, market_data_service):
        self.market_data_service = market_data_service

    def run(self, user_profile):
        holdings = user_profile.holdings

        if not holdings:
            benchmark = self.market_data_service.benchmark_label(
                self.market_data_service.benchmark_for_user(user_profile)
            )
            return PortfolioHealthResponse(
                concentration_risk=ConcentrationRisk(flag="none"),
                performance=PerformanceMetrics(total_return_pct=None, annualized_return_pct=None),
                benchmark_comparison=BenchmarkComparison(
                    benchmark=benchmark,
                    portfolio_return_pct=None,
                    benchmark_return_pct=None,
                    alpha_pct=None,
                ),
                observations=[
                    Observation(
                        severity="info",
                        text="You do not hold any investments yet, so there is no diversification or performance risk to assess.",
                    ),
                    Observation(
                        severity="info",
                        text="A sensible next step is to define your goal, time horizon, and risk tolerance before making a first allocation.",
                    ),
                ],
                disclaimer=DISCLAIMER,
                metadata={"build_oriented": True},
            )


        weights_map = self.market_data_service.holding_weights(holdings)
        weights = sorted(weights_map.values(), reverse=True)
        top_position = round(weights[0], 2) if weights else 0.0
        top3 = round(sum(weights[:3]), 2) if weights else 0.0

        if top_position >= 50 or top3 >= 75:
            flag = "high"
        elif top_position >= 25 or top3 >= 55:
            flag = "warning"
        else:
            flag = "low"

        
        benchmark_label = self.market_data_service.benchmark_for_user(user_profile)
        portfolio_return = self.market_data_service.portfolio_return_pct(holdings)
        benchmark_return = self.market_data_service.benchmark_return_pct(benchmark_label)
        annualized = self.market_data_service.annualized_return(portfolio_return)



        alpha = None
        if portfolio_return is not None and benchmark_return is not None:
            alpha = round(portfolio_return - benchmark_return, 2)

        top_holding = max(weights_map, key=weights_map.get) if weights_map else holdings[0].ticker

        observations = []
        if top_position >= 50:
            observations.append(
                Observation(
                    severity="critical",
                    text=f"{top_position}% of your portfolio is in {top_holding}, which is a very high concentration risk.",
                )
            )
        elif top_position >= 25:
            observations.append(
                Observation(
                    severity="warning",
                    text=f"{top_position}% of your portfolio is in {top_holding}, which may reduce diversification.",
                )
            )
        else:
            observations.append(
                Observation(
                    severity="info",
                    text="Your largest position size is moderate relative to the rest of the portfolio.",
                )
            )

        if alpha is not None:
            if alpha >= 0:
                observations.append(
                    Observation(
                        severity="info",
                        text=f"Your portfolio is currently ahead of the {benchmark_label} by {alpha} percentage points over the measured period.",
                    )
                )
            else:
                observations.append(
                    Observation(
                        severity="warning",
                        text=f"Your portfolio is trailing the {benchmark_label} by {abs(alpha)} percentage points over the measured period.",
                    )
                )

        if ((user_profile.metadata.get("preferences") or {}).get("income_focus")):
            observations.append(
                Observation(
                    severity="info",
                    text="Your holdings suggest an income focus, so dividend stability and interest-rate sensitivity matter more than short-term price moves.",
                )
            )

        return PortfolioHealthResponse(
            concentration_risk=ConcentrationRisk(
                top_position_pct=top_position,
                top_3_positions_pct=top3,
                flag=flag,
            ),
            performance=PerformanceMetrics(
                total_return_pct=portfolio_return,
                annualized_return_pct=annualized,
            ),
            benchmark_comparison=BenchmarkComparison(
                benchmark=benchmark_label,
                portfolio_return_pct=portfolio_return,
                benchmark_return_pct=benchmark_return,
                alpha_pct=alpha,
            ),
            observations=observations,
            disclaimer=DISCLAIMER,
        )


# def run(user, llm=None):
#     from src.services.market_data import MarketDataService
#     agent = PortfolioHealthAgent(MarketDataService())
#     return agent.run(user).model_dump()

def run(user, llm=None):
    from src.services.market_data import MarketDataService
    normalized_user = _coerce_user(user)
    agent = PortfolioHealthAgent(MarketDataService())
    return agent.run(normalized_user).model_dump()