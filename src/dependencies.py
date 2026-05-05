# # from pathlib import Path
# # import json

# # from src.agents.portfolio_health import PortfolioHealthAgent
# # from src.agents.stub import StubAgent
# # from src.classifier.client import OpenAIClassifierClient
# # from src.classifier.service import ClassifierService
# # from src.models.domain import Holding, UserProfile
# # from src.router.agent_router import AgentRouter
# # from src.safety.guard import SafetyGuard
# # from src.services.market_data import MarketDataService
# # from src.services.orchestrator import Orchestrator
# # from src.services.session_store import InMemorySessionStore

# # _SESSION_STORE = InMemorySessionStore()


# # def load_user_profile(user_id: str) -> UserProfile:
# #     fixtures_dir = Path("fixtures/users")

# #     if fixtures_dir.exists():
# #         for file in fixtures_dir.glob("*.json"):
# #             data = json.loads(file.read_text(encoding="utf-8"))
# #             if data.get("user_id") == user_id:
# #                 raw_holdings = data.get("holdings", []) or data.get("portfolio", {}).get("holdings", [])
# #                 holdings = [
# #                     Holding(
# #                         ticker=h.get("ticker") or h.get("symbol") or "UNKNOWN",
# #                         quantity=h.get("quantity", h.get("shares", 0.0)),
# #                         avg_cost=h.get("avg_cost", h.get("average_cost")),
# #                         currency=h.get("currency"),
# #                         market=h.get("market"),
# #                         sector=h.get("sector"),
# #                         weight_pct=h.get("weight_pct", h.get("weight")),
# #                         metadata=h,
# #                     )
# #                     for h in raw_holdings
# #                 ]

# #                 return UserProfile(
# #                     user_id=data.get("user_id", user_id),
# #                     name=data.get("name"),
# #                     country=data.get("country") or data.get("location", {}).get("country"),
# #                     base_currency=data.get("base_currency") or data.get("currency"),
# #                     risk_profile=data.get("risk_profile"),
# #                     kyc_status=data.get("kyc_status"),
# #                     investment_objective=data.get("investment_objective"),
# #                     holdings=holdings,
# #                     metadata=data,
# #                 )

# #     return UserProfile(user_id=user_id, holdings=[])


# # def get_orchestrator() -> Orchestrator:
# #     market_data = MarketDataService()
# #     portfolio_agent = PortfolioHealthAgent(market_data)
# #     stub_agent = StubAgent()
# #     router = AgentRouter(portfolio_agent, stub_agent)
# #     classifier = ClassifierService(OpenAIClassifierClient())

# #     return Orchestrator(
# #         safety_guard=SafetyGuard(),
# #         classifier_service=classifier,
# #         agent_router=router,
# #         session_store=_SESSION_STORE,
# #         user_loader=load_user_profile,
# #     )





# from pathlib import Path
# import json

# from src.agents.portfolio_health import PortfolioHealthAgent
# from src.agents.stub import StubAgent
# from src.classifier.client import OpenAIClassifierClient
# from src.classifier.service import ClassifierService
# from src.models.domain import Holding, UserProfile
# from src.router.agent_router import AgentRouter
# from src.safety.guard import SafetyGuard
# from src.services.market_data import MarketDataService
# from src.services.orchestrator import Orchestrator
# from src.services.session_store import InMemorySessionStore

# _SESSION_STORE = InMemorySessionStore()


# def load_user_profile(user_id: str) -> UserProfile:
#     fixtures_dir = Path("fixtures/users")

#     if fixtures_dir.exists():
#         for file in fixtures_dir.glob("*.json"):
#             data = json.loads(file.read_text(encoding="utf-8"))
#             if data.get("user_id") == user_id:
#                 raw_positions = data.get("positions", [])
#                 holdings = [
#                     Holding(
#                         ticker=pos.get("ticker", "UNKNOWN"),
#                         quantity=pos.get("quantity", 0.0),
#                         avg_cost=pos.get("avg_cost"),
#                         currency=pos.get("currency"),
#                         market=pos.get("exchange"),
#                         sector=pos.get("sector"),
#                         weight_pct=pos.get("weight_pct", pos.get("weight")),
#                         metadata=pos,
#                     )
#                     for pos in raw_positions
#                 ]

#                 return UserProfile(
#                     user_id=data.get("user_id", user_id),
#                     name=data.get("name"),
#                     country=data.get("country"),
#                     base_currency=data.get("base_currency"),
#                     risk_profile=data.get("risk_profile"),
#                     kyc_status=(data.get("kyc") or {}).get("status"),
#                     investment_objective=(data.get("preferences") or {}).get("goal"),
#                     holdings=holdings,
#                     metadata=data,
#                 )

#     return UserProfile(user_id=user_id, holdings=[])


# def get_orchestrator() -> Orchestrator:
#     market_data = MarketDataService()
#     portfolio_agent = PortfolioHealthAgent(market_data)
#     stub_agent = StubAgent()
#     router = AgentRouter(portfolio_agent, stub_agent)
#     classifier = ClassifierService(OpenAIClassifierClient())

#     return Orchestrator(
#         safety_guard=SafetyGuard(),
#         classifier_service=classifier,
#         agent_router=router,
#         session_store=_SESSION_STORE,
#         user_loader=load_user_profile,
#     )
















from pathlib import Path
import json

from src.agents.portfolio_health import PortfolioHealthAgent
from src.agents.stub import StubAgent
from src.classifier.client import OpenAIClassifierClient
from src.classifier.service import ClassifierService
from src.models.domain import Holding, UserProfile
from src.router.agent_router import AgentRouter
from src.safety.guard import SafetyGuard
from src.services.market_data import MarketDataService
from src.services.orchestrator import Orchestrator
from src.services.session_store import InMemorySessionStore

_SESSION_STORE = InMemorySessionStore()


def load_user_profile(user_id: str) -> UserProfile:
    fixtures_dir = Path("fixtures/users")

    if fixtures_dir.exists():
        for file in fixtures_dir.glob("*.json"):
            data = json.loads(file.read_text(encoding="utf-8"))
            if data.get("user_id") == user_id:
                raw_positions = data.get("positions", [])
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
                    user_id=data.get("user_id", user_id),
                    name=data.get("name"),
                    age=data.get("age"),
                    country=data.get("country"),
                    base_currency=data.get("base_currency"),
                    risk_profile=data.get("risk_profile"),
                    kyc_status=(data.get("kyc") or {}).get("status"),
                    investment_objective=((data.get("preferences") or {}).get("goal")),
                    holdings=holdings,
                    metadata=data,
                )

    return UserProfile(user_id=user_id, holdings=[])


def get_orchestrator() -> Orchestrator:
    market_data = MarketDataService()
    portfolio_agent = PortfolioHealthAgent(market_data)
    stub_agent = StubAgent()
    router = AgentRouter(portfolio_agent, stub_agent)
    classifier = ClassifierService(OpenAIClassifierClient())

    return Orchestrator(
        safety_guard=SafetyGuard(),
        classifier_service=classifier,
        agent_router=router,
        session_store=_SESSION_STORE,
        user_loader=load_user_profile,
    )