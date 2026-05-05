
# import re
# from src.models.classification import ClassificationResult, ExtractedEntities

# TICKER_RE = re.compile(r"\b[A-Z]{1,5}(?:\.[A-Z]{1,3})?\b")

# def extract_entities(text: str) -> ExtractedEntities:
#     lower = text.lower()
#     tickers = list({m.group(0).upper() for m in TICKER_RE.finditer(text)})
#     topics, sectors = [], []

#     topic_map = [
#         ("mutual fund", "mutual fund"),
#         ("compound interest", "compound interest"),
#         ("etf", "ETF"),
#         ("index fund", "index fund"),
#         ("p/e ratio", "P/E ratio"),
#         ("beta", "beta"),
#         ("max drawdown", "max drawdown"),
#         ("recession", "recession"),
#         ("login", "login"),
#         ("bank account", "bank account"),
#         ("transaction history", "transaction history"),
#         ("recurring investment", "recurring investment"),
#         ("fx", "FX"),
#     ]
#     for needle, label in topic_map:
#         if needle in lower:
#             topics.append(label)

#     if "tech" in lower or "technology" in lower:
#         sectors.append("technology")
#     if "emerging market" in lower:
#         topics.append("emerging markets")
#     if "dividend" in lower:
#         topics.append("dividend")
#     if "world" in lower:
#         topics.append("world")

#     amount = None
#     rate = None
#     period_years = None
#     currency = None
#     index = None
#     action = None
#     goal = None
#     frequency = None
#     horizon = None
#     time_period = None

#     amt = re.search(r"\b(\d[\d,]*(?:\.\d+)?)\b", text)
#     if amt:
#         amount = float(amt.group(1).replace(",", ""))

#     if "%" in text or " at 8" in lower or " 6.5" in lower:
#         r = re.search(r"(\d+(?:\.\d+)?)\s*%", text)
#         if r:
#             rate = float(r.group(1)) / 100.0

#     y = re.search(r"(\d+)\s*years?", lower)
#     if y:
#         period_years = int(y.group(1))

#     for ccy in ["USD", "EUR", "GBP", "JPY"]:
#         if ccy.lower() in lower:
#             currency = ccy

#     if "s&p 500" in lower or "s&p500" in lower:
#         index = "S&P 500"
#     elif "ftse 100" in lower:
#         index = "FTSE 100"
#     elif "nikkei" in lower:
#         index = "NIKKEI 225"
#     elif "msci world" in lower:
#         index = "MSCI World"

#     for a in ["buy", "sell", "hold", "hedge", "rebalance"]:
#         if a in lower:
#             action = a
#             break

#     for g in ["retirement", "education", "house", "fire", "emergency_fund"]:
#         if g in lower:
#             goal = g
#             break

#     for f in ["daily", "weekly", "monthly", "yearly"]:
#         if f in lower:
#             frequency = f
#             break

#     if "6 months" in lower:
#         horizon = "6_months"
#     elif "1 year" in lower:
#         horizon = "1_year"
#     elif "5 years" in lower:
#         horizon = "5_years"

#     if "today" in lower:
#         time_period = "today"
#     elif "this week" in lower:
#         time_period = "this_week"
#     elif "this month" in lower:
#         time_period = "this_month"
#     elif "this year" in lower:
#         time_period = "this_year"

#     return ExtractedEntities(
#         tickers=tickers,
#         topics=topics,
#         sectors=sectors,
#         amount=amount,
#         rate=rate,
#         period_years=period_years,
#         currency=currency,
#         index=index,
#         action=action,
#         goal=goal,
#         frequency=frequency,
#         horizon=horizon,
#         time_period=time_period,
#     )

# def route_query(query: str) -> tuple[str, str]:
#     q = " ".join(query.lower().split())

#     if q in {"hi", "hello", "thanks", "abcdefg"}:
#         return "general_query", "general_query"

#     if any(p in q for p in [
#         "how is my portfolio doing", "health check on my investments", "well diversified",
#         "concentration risk", "beating the market", "review my holdings", "portfolio summary"
#     ]):
#         return "portfolio_health", "portfolio_health"

#     if any(p in q for p in [
#         "what's the price of", "tell me about", "any news on", "how is tesla doing",
#         "compare hsbc and barclays", "what happened in markets today", "top gainers in s&p 500",
#         "gold price", "eur/usd rate", "how is the ftse doing", "what's happening with the nikkei"
#     ]):
#         return "market_research", "market_research"

#     if any(p in q for p in [
#         "should i sell", "should i buy", "good time to invest", "rebalance my portfolio",
#         "equity-bond split", "should i hedge"
#     ]):
#         return "investment_strategy", "investment_strategy"

#     if any(p in q for p in [
#         "save for retirement", "retire at", "college fund", "house down payment", "fire plan"
#     ]):
#         return "financial_planning", "financial_planning"

#     if any(p in q for p in [
#         "invest", "calculate mortgage", "future value", "convert", "compound returns"
#     ]):
#         return "financial_calculator", "financial_calculator"

#     if any(p in q for p in [
#         "downside risk", "beta", "max drawdown", "stress test", "exposed am i"
#     ]):
#         return "risk_assessment", "risk_assessment"

#     if any(p in q for p in [
#         "recommend a large cap etf", "which fund should i buy", "best low-cost world index fund", "recommend a dividend etf"
#     ]):
#         return "product_recommendation", "product_recommendation"

#     if any(p in q for p in ["where will", "predict", "forecast", "in 6 months", "in 5 years"]):
#         return "predictive_analysis", "predictive_analysis"

#     if any(p in q for p in [
#         "can't login", "linked bank account", "transaction history", "recurring investment"
#     ]):
#         return "customer_support", "customer_support"

#     return "general_query", "general_query"

# class ClassifierService:
#     def __init__(self, llm_client=None):
#         self.llm_client = llm_client

#     def classify(self, query: str, prior_turns: list[str]) -> ClassificationResult:
#         text = " ".join(prior_turns + [query])
#         intent, agent = route_query(text)
#         return ClassificationResult(
#             intent=intent,
#             target_agent=agent,
#             extracted_entities=extract_entities(text),
#             safety_verdict="unknown",
#         )

# def classify(query: str, llm=None, prior_turns: list[str] | None = None) -> ClassificationResult:
#     return ClassifierService().classify(query, prior_turns or [])















# import re
# from src.models.classification import ClassificationResult, ExtractedEntities

# # TICKER_RE = re.compile(r"\b[A-Z]{2,5}(?:\.[A-Z]{1,3})?\b")
# # BLACKLIST_TICKERS = {"AN", "AND", "ARE", "FOR", "THE", "USD", "EUR", "GBP", "JPY"}

# # NAME_TO_TICKER = {
# #     "apple": "AAPL",
# #     "nvidia": "NVDA",
# #     "tesla": "TSLA",
# #     "microsoft": "MSFT",
# #     "hsbc": "HSBA.L",
# #     "barclays": "BARC.L",
# #     "asml": "ASML.AS",
# # }

# TICKER_RE = re.compile(r"\b[A-Z]{2,5}(?:\.[A-Z]{1,3})?\b")

# BLACKLIST_TICKERS = {"AN", "AND", "ARE", "FOR", "THE", "USD", "EUR", "GBP", "JPY"}

# NAME_TO_TICKER = {
#     "apple": "AAPL",
#     "nvidia": "NVDA",
#     "tesla": "TSLA",
#     "microsoft": "MSFT",
#     "hsbc": "HSBA.L",
#     "barclays": "BARC.L",
#     "asml": "ASML.AS",
#     "toyota": "7203.T",
# }

# def extract_entities(text: str) -> ExtractedEntities:
#     lower = " ".join(text.lower().split())
#     tickers = sorted({
#         m.group(0).upper()
#         for m in TICKER_RE.finditer(text)
#         if m.group(0).upper() not in BLACKLIST_TICKERS
#     })
#     for name, ticker in NAME_TO_TICKER.items():
#         if name in lower and ticker not in tickers:
#             tickers.append(ticker)

#     topics, sectors = [], []
#     topic_map = [
#         ("mutual fund", "mutual fund"),
#         ("compound interest", "compound interest"),
#         ("etf", "ETF"),
#         ("index fund", "index fund"),
#         ("p/e ratio", "P/E ratio"),
#         ("beta", "beta"),
#         ("max drawdown", "max drawdown"),
#         ("recession", "recession"),
#         ("login", "login"),
#         ("bank account", "bank account"),
#         ("transaction history", "transaction history"),
#         ("recurring investment", "recurring investment"),
#         ("fx", "FX"),
#         ("lctg", "LTCG"),
#     ]
#     for needle, label in topic_map:
#         if needle in lower and label not in topics:
#             topics.append(label)

#     if "tech" in lower or "technology" in lower:
#         sectors.append("technology")
#     if "emerging market" in lower:
#         topics.append("emerging markets")
#     if "dividend" in lower:
#         topics.append("dividend")
#     if "world" in lower:
#         topics.append("world")

#     amount = None
#     rate = None
#     period_years = None
#     currency = None
#     index = None
#     action = None
#     goal = None
#     frequency = None
#     horizon = None
#     time_period = None

#     amt = re.search(r"\b(\d[\d,]*(?:\.\d+)?)\b", text)
#     if amt:
#         amount = float(amt.group(1).replace(",", ""))

#     r = re.search(r"(\d+(?:\.\d+)?)\s*%", text)
#     if r:
#         rate = float(r.group(1)) / 100.0

#     y = re.search(r"(\d+)\s*years?", lower)
#     if y:
#         period_years = int(y.group(1))

#     for ccy in ["USD", "EUR", "GBP", "JPY"]:
#         if ccy.lower() in lower:
#             currency = ccy
#             break

#     if "s&p 500" in lower or "s&p500" in lower:
#         index = "S&P 500"
#     elif "ftse 100" in lower:
#         index = "FTSE 100"
#     elif "nikkei" in lower:
#         index = "NIKKEI 225"
#     elif "msci world" in lower:
#         index = "MSCI World"

#     for a in ["buy", "sell", "hold", "hedge", "rebalance"]:
#         if a in lower:
#             action = a
#             break

#     for g in ["retirement", "education", "house", "fire", "emergency_fund"]:
#         if g in lower:
#             goal = g
#             break

#     for f in ["daily", "weekly", "monthly", "yearly"]:
#         if f in lower:
#             frequency = f
#             break

#     if "6 months" in lower:
#         horizon = "6_months"
#     elif "1 year" in lower:
#         horizon = "1_year"
#     elif "5 years" in lower:
#         horizon = "5_years"

#     if "today" in lower:
#         time_period = "today"
#     elif "this week" in lower:
#         time_period = "this_week"
#     elif "this month" in lower:
#         time_period = "this_month"
#     elif "this year" in lower:
#         time_period = "this_year"

#     return ExtractedEntities(
#         tickers=tickers,
#         topics=topics,
#         sectors=sectors,
#         amount=amount,
#         rate=rate,
#         period_years=period_years,
#         currency=currency,
#         index=index,
#         action=action,
#         goal=goal,
#         frequency=frequency,
#         horizon=horizon,
#         time_period=time_period,
#     )
# def route_query(query: str) -> tuple[str, str]:
#     q = " ".join(query.lower().split())

#     if q in {"hi", "hello", "thanks", "abcdefg"}:
#         return "general_query", "general_query"

#     if any(p in q for p in [
#         "how is my portfolio doing", "health check on my investments", "well diversified",
#         "concentration risk", "beating the market", "review my holdings", "portfolio summary"
#     ]):
#         return "portfolio_health", "portfolio_health"

#     if any(p in q for p in [
#         "what's the price of", "tell me about", "any news on", "how is tesla doing",
#         "compare hsbc and barclays", "what happened in markets today", "top gainers in s&p 500",
#         "gold price", "eur/usd rate", "how is the ftse doing", "what's happening with the nikkei"
#     ]):
#         return "market_research", "market_research"

#     if any(p in q for p in [
#         "should i sell", "should i buy", "good time to invest", "rebalance my portfolio",
#         "equity-bond split", "should i hedge"
#     ]):
#         return "investment_strategy", "investment_strategy"

#     if any(p in q for p in [
#         "save for retirement", "retire at", "college fund", "house down payment", "fire plan"
#     ]):
#         return "financial_planning", "financial_planning"

#     if any(p in q for p in [
#         "invest", "calculate mortgage", "future value", "convert", "compound returns"
#     ]):
#         return "financial_calculator", "financial_calculator"

#     if any(p in q for p in [
#         "downside risk", "beta", "max drawdown", "stress test", "exposed am i"
#     ]):
#         return "risk_assessment", "risk_assessment"

#     if any(p in q for p in [
#         "recommend a large cap etf", "which fund should i buy", "best low-cost world index fund", "recommend a dividend etf"
#     ]):
#         return "product_recommendation", "product_recommendation"

#     if any(p in q for p in ["where will", "predict", "forecast", "in 6 months", "in 5 years"]):
#         return "predictive_analysis", "predictive_analysis"

#     if any(p in q for p in [
#         "can't login", "linked bank account", "transaction history", "recurring investment"
#     ]):
#         return "customer_support", "customer_support"

#     return "general_query", "general_query"

# class ClassifierService:
#     def __init__(self, llm_client=None):
#         self.llm_client = llm_client

#     def classify(self, query: str, prior_turns: list[str]) -> ClassificationResult:
#         text = " ".join(prior_turns + [query])
#         intent, agent = route_query(text)
#         return ClassificationResult(
#             intent=intent,
#             target_agent=agent,
#             extracted_entities=extract_entities(text),
#             safety_verdict="unknown",
#         )

# def classify(query: str, llm=None, prior_turns: list[str] | None = None) -> ClassificationResult:
#     return ClassifierService().classify(query, prior_turns or [])









# import re
# from src.models.classification import ClassificationResult, ExtractedEntities

# # -----------------------------
# # Regex + dictionaries
# # -----------------------------

# TICKER_RE = re.compile(r"\b[A-Z]{2,5}(?:\.[A-Z]{1,3})?\b")

# BLACKLIST_TICKERS = {
#     "AN", "AND", "ARE", "FOR", "THE",
#     "USD", "EUR", "GBP", "JPY"
# }

# NAME_TO_TICKER = {
#     "apple": "AAPL",
#     "nvidia": "NVDA",
#     "tesla": "TSLA",
#     "microsoft": "MSFT",
#     "hsbc": "HSBA.L",
#     "barclays": "BARC.L",
#     "asml": "ASML.AS",
#     "toyota": "7203.T",
# }


# # -----------------------------
# # Entity extraction
# # -----------------------------
# def extract_entities(text: str) -> ExtractedEntities:
#     lower = " ".join(text.lower().split())

#     # ---- tickers (regex + blacklist)
#     tickers = {
#         m.group(0).upper()
#         for m in TICKER_RE.finditer(text)
#         if m.group(0).upper() not in BLACKLIST_TICKERS
#     }

#     # ---- company name mapping
#     for name, ticker in NAME_TO_TICKER.items():
#         if name in lower:
#             tickers.add(ticker)

#     tickers = sorted(tickers)

#     # ---- topics
#     topics = []
#     topic_map = [
#         ("mutual fund", "mutual fund"),
#         ("compound interest", "compound interest"),
#         ("etf", "ETF"),
#         ("index fund", "index fund"),
#         ("p/e ratio", "P/E ratio"),
#         ("beta", "beta"),
#         ("max drawdown", "max drawdown"),
#         ("recession", "recession"),
#         ("login", "login"),
#         ("bank account", "bank account"),
#         ("transaction history", "transaction history"),
#         ("recurring investment", "recurring investment"),
#         ("fx", "FX"),
#         ("ltcg", "LTCG"),
#     ]

#     for k, v in topic_map:
#         if k in lower:
#             topics.append(v)

#     # ---- sectors
#     sectors = []
#     if "tech" in lower or "technology" in lower:
#         sectors.append("technology")

#     # ---- numeric parsing
#     amount = None
#     rate = None
#     period_years = None

#     amt = re.search(r"\b(\d[\d,]*(?:\.\d+)?)\b", text)
#     if amt:
#         amount = float(amt.group(1).replace(",", ""))

#     r = re.search(r"(\d+(?:\.\d+)?)\s*%", text)
#     if r:
#         rate = float(r.group(1)) / 100.0

#     y = re.search(r"(\d+)\s*years?", lower)
#     if y:
#         period_years = int(y.group(1))

#     # ---- currency
#     currency = None
#     for ccy in ["USD", "EUR", "GBP", "JPY"]:
#         if ccy.lower() in lower:
#             currency = ccy
#             break

#     # ---- index
#     index = None
#     if "s&p 500" in lower or "s&p500" in lower:
#         index = "S&P 500"
#     elif "ftse 100" in lower:
#         index = "FTSE 100"
#     elif "nikkei" in lower:
#         index = "NIKKEI 225"
#     elif "msci world" in lower:
#         index = "MSCI World"

#     # ---- action
#     action = next((a for a in ["buy", "sell", "hold", "hedge", "rebalance"] if a in lower), None)

#     # ---- goal
#     goal = next((g for g in ["retirement", "education", "house", "fire", "emergency_fund"] if g in lower), None)

#     # ---- frequency / horizon / time
#     frequency = next((f for f in ["daily", "weekly", "monthly", "yearly"] if f in lower), None)

#     horizon = None
#     if "6 months" in lower:
#         horizon = "6_months"
#     elif "1 year" in lower:
#         horizon = "1_year"
#     elif "5 years" in lower:
#         horizon = "5_years"

#     time_period = None
#     if "today" in lower:
#         time_period = "today"
#     elif "this week" in lower:
#         time_period = "this_week"
#     elif "this month" in lower:
#         time_period = "this_month"
#     elif "this year" in lower:
#         time_period = "this_year"

#     return ExtractedEntities(
#         tickers=tickers,
#         topics=topics,
#         sectors=sectors,
#         amount=amount,
#         rate=rate,
#         period_years=period_years,
#         currency=currency,
#         index=index,
#         action=action,
#         goal=goal,
#         frequency=frequency,
#         horizon=horizon,
#         time_period=time_period,
#     )


# # -----------------------------
# # Routing logic (FIXED ORDER)
# # -----------------------------
# # def route_query(query: str, entities: ExtractedEntities = None) -> tuple[str, str]:
# #     q = " ".join(query.lower().split())

# #     # 1. greetings / junk first
# #     if q in {"hi", "hello", "thanks", "abcdefg"}:
# #         return "general_query", "general_query"

# #     # 2. portfolio
# #     if any(p in q for p in [
# #         "how is my portfolio doing",
# #         "health check on my investments",
# #         "concentration risk",
# #         "review my holdings",
# #         "portfolio summary",
# #         "beating the market"
# #     ]):
# #         return "portfolio_health", "portfolio_health"

# #     # 3. market research
# #     if any(p in q for p in [
# #         "price of", "tell me about", "news on",
# #         "markets today", "top gainers", "gold price",
# #         "eur/usd", "ftse", "nikkei"
# #     ]):
# #         return "market_research", "market_research"

# #     # 4. IMPORTANT FIX: ticker/name shortcut routing
# #     if entities and entities.tickers and len(q.split()) <= 3:
# #         return "market_research", "market_research"

# #     # 5. strategy
# #     if any(p in q for p in [
# #         "should i sell", "should i buy", "rebalance",
# #         "hedge", "invest in"
# #     ]):
# #         return "investment_strategy", "investment_strategy"

# #     # 6. planning
# #     if any(p in q for p in [
# #         "retire", "retirement", "college fund",
# #         "house down payment", "fire plan"
# #     ]):
# #         return "financial_planning", "financial_planning"

# #     # 7. calculator
# #     if any(p in q for p in [
# #         "calculate", "future value", "mortgage", "convert"
# #     ]):
# #         return "financial_calculator", "financial_calculator"

# #     # 8. risk
# #     if any(p in q for p in [
# #         "drawdown", "beta", "risk", "stress test"
# #     ]):
# #         return "risk_assessment", "risk_assessment"

# #     # 9. fallback
# #     return "general_query", "general_query"


# # # -----------------------------
# # # Classifier service
# # # -----------------------------
# # class ClassifierService:
# #     def __init__(self, llm_client=None):
# #         self.llm_client = llm_client

# #     def classify(self, query: str, prior_turns: list[str]) -> ClassificationResult:
# #         text = " ".join(prior_turns + [query])

# #         entities = extract_entities(text)
# #         intent, agent = route_query(text, entities)

# #         return ClassificationResult(
# #             intent=intent,
# #             target_agent=agent,
# #             extracted_entities=entities,
# #             safety_verdict="unknown",
# #         )


# # def classify(query: str, llm=None, prior_turns: list[str] | None = None):
# #     return ClassifierService().classify(query, prior_turns or [])





# def route_query(query: str, entities: ExtractedEntities | None = None) -> tuple[str, str]:
#     q = " ".join(query.lower().split())
#     entities = entities or extract_entities(query)

#     if q in {"hi", "hello", "thanks", "abcdefg"}:
#         return "general_query", "general_query"

#     if any(p in q for p in [
#         "how is my portfolio doing",
#         "health check on my investments",
#         "well diversified",
#         "concentration risk",
#         "beating the market",
#         "review my holdings",
#         "portfolio summary",
#         "am i diversified",
#         "portfolio health",
#         "how risky is my portfolio"
#     ]):
#         return "portfolio_health", "portfolio_health"

#     if any(p in q for p in [
#         "can't login",
#         "cant login",
#         "linked bank account",
#         "bank account",
#         "transaction history",
#         "recurring investment",
#         "deposit failed",
#         "withdrawal failed"
#     ]):
#         return "customer_support", "customer_support"

#     if any(p in q for p in [
#         "should i sell",
#         "should i buy",
#         "good time to invest",
#         "rebalance my portfolio",
#         "equity-bond split",
#         "should i hedge",
#         "sell my",
#         "buy more",
#         "what should i do with"
#     ]):
#         return "investment_strategy", "investment_strategy"

#     if any(p in q for p in [
#         "save for retirement",
#         "retire at",
#         "college fund",
#         "house down payment",
#         "fire plan",
#         "retirement",
#         "goal planning",
#         "how much do i need"
#     ]):
#         return "financial_planning", "financial_planning"

#     if any(p in q for p in [
#         "calculate mortgage",
#         "future value",
#         "convert",
#         "compound interest",
#         "if i invest",
#         "how much if",
#         "what will i have",
#         "emi",
#         "loan",
#         "calculator"
#     ]):
#         return "financial_calculator", "financial_calculator"

#     if any(p in q for p in [
#         "downside risk",
#         "beta",
#         "max drawdown",
#         "stress test",
#         "risk",
#         "volatility",
#         "drawdown",
#         "exposed am i"
#     ]):
#         return "risk_assessment", "risk_assessment"

#     if any(p in q for p in [
#         "recommend a large cap etf",
#         "which fund should i buy",
#         "best low-cost world index fund",
#         "recommend a dividend etf",
#         "fund recommendation",
#         "product recommendation",
#         "best etf"
#     ]):
#         return "product_recommendation", "product_recommendation"

#     if any(p in q for p in [
#         "where will",
#         "predict",
#         "forecast",
#         "in 6 months",
#         "in 5 years",
#         "next year",
#         "future outlook",
#         "what happens if"
#     ]):
#         return "predictive_analysis", "predictive_analysis"

#     if any(p in q for p in [
#         "price of",
#         "tell me about",
#         "news on",
#         "markets today",
#         "top gainers",
#         "gold price",
#         "eur/usd",
#         "ftse",
#         "nikkei",
#         "apple",
#         "nvidia",
#         "tesla",
#         "microsoft",
#         "hsbc",
#         "barclays",
#         "asml"
#     ]):
#         return "market_research", "market_research"

#     if entities.tickers and len(q.split()) <= 3:
#         return "market_research", "market_research"

#     return "general_query", "general_query"


















import re
from src.models.classification import ClassificationResult, ExtractedEntities

TICKER_RE = re.compile(r"\b[A-Z]{2,5}(?:\.[A-Z]{1,3})?\b")

BLACKLIST_TICKERS = {
    "AN", "AND", "ARE", "FOR", "THE",
    "USD", "EUR", "GBP", "JPY",
}

NAME_TO_TICKER = {
    "apple": "AAPL",
    "nvidia": "NVDA",
    "tesla": "TSLA",
    "microsoft": "MSFT",
    "hsbc": "HSBA.L",
    "barclays": "BARC.L",
    "asml": "ASML.AS",
    "toyota": "7203.T",
}


def extract_entities(text: str) -> ExtractedEntities:
    lower = " ".join(text.lower().split())

    tickers = {
        m.group(0).upper()
        for m in TICKER_RE.finditer(text)
        if m.group(0).upper() not in BLACKLIST_TICKERS
    }

    for name, ticker in NAME_TO_TICKER.items():
        if name in lower:
            tickers.add(ticker)

    tickers = sorted(tickers)

    topics = []
    topic_map = [
        ("mutual fund", "mutual fund"),
        ("compound interest", "compound interest"),
        ("etf", "ETF"),
        ("index fund", "index fund"),
        ("p/e ratio", "P/E ratio"),
        ("beta", "beta"),
        ("max drawdown", "max drawdown"),
        ("recession", "recession"),
        ("login", "login"),
        ("bank account", "bank account"),
        ("transaction history", "transaction history"),
        ("recurring investment", "recurring investment"),
        ("fx", "FX"),
        ("ltcg", "LTCG"),
    ]
    for k, v in topic_map:
        if k in lower and v not in topics:
            topics.append(v)

    sectors = []
    if "tech" in lower or "technology" in lower:
        sectors.append("technology")

    amount = None
    rate = None
    period_years = None

    amt = re.search(r"\b(\d[\d,]*(?:\.\d+)?)\b", text)
    if amt:
        amount = float(amt.group(1).replace(",", ""))

    r = re.search(r"(\d+(?:\.\d+)?)\s*%", text)
    if r:
        rate = float(r.group(1)) / 100.0

    y = re.search(r"(\d+)\s*years?", lower)
    if y:
        period_years = int(y.group(1))

    currency = None
    for ccy in ["USD", "EUR", "GBP", "JPY"]:
        if ccy.lower() in lower:
            currency = ccy
            break

    index = None
    if "s&p 500" in lower or "s&p500" in lower:
        index = "S&P 500"
    elif "ftse 100" in lower:
        index = "FTSE 100"
    elif "nikkei" in lower:
        index = "NIKKEI 225"
    elif "msci world" in lower:
        index = "MSCI World"

    action = next((a for a in ["buy", "sell", "hold", "hedge", "rebalance"] if a in lower), None)
    goal = next((g for g in ["retirement", "education", "house", "fire", "emergency_fund"] if g in lower), None)
    frequency = next((f for f in ["daily", "weekly", "monthly", "yearly"] if f in lower), None)

    horizon = None
    if "6 months" in lower:
        horizon = "6_months"
    elif "1 year" in lower:
        horizon = "1_year"
    elif "5 years" in lower:
        horizon = "5_years"

    time_period = None
    if "today" in lower:
        time_period = "today"
    elif "this week" in lower:
        time_period = "this_week"
    elif "this month" in lower:
        time_period = "this_month"
    elif "this year" in lower:
        time_period = "this_year"

    return ExtractedEntities(
        tickers=tickers,
        topics=topics,
        sectors=sectors,
        amount=amount,
        rate=rate,
        period_years=period_years,
        currency=currency,
        index=index,
        action=action,
        goal=goal,
        frequency=frequency,
        horizon=horizon,
        time_period=time_period,
    )


def route_query(query: str, entities: ExtractedEntities | None = None) -> tuple[str, str]:
    q = " ".join(query.lower().split())
    entities = entities or extract_entities(query)

    if q in {"hi", "hello", "thanks", "abcdefg"}:
        return "general_query", "general_query"

    if any(p in q for p in [
        "how is my portfolio doing",
        "health check on my investments",
        "well diversified",
        "concentration risk",
        "beating the market",
        "review my holdings",
        "portfolio summary",
        "am i diversified",
        "portfolio health",
        "how risky is my portfolio",
    ]):
        return "portfolio_health", "portfolio_health"

    if any(p in q for p in [
        "can't login",
        "cant login",
        "linked bank account",
        "bank account",
        "transaction history",
        "recurring investment",
        "deposit failed",
        "withdrawal failed",
    ]):
        return "customer_support", "customer_support"

    if any(p in q for p in [
        "should i sell",
        "should i buy",
        "good time to invest",
        "rebalance my portfolio",
        "equity-bond split",
        "should i hedge",
        "sell my",
        "buy more",
        "what should i do with",
    ]):
        return "investment_strategy", "investment_strategy"

    if any(p in q for p in [
        "save for retirement",
        "retire at",
        "college fund",
        "house down payment",
        "fire plan",
        "retirement",
        "goal planning",
        "how much do i need",
    ]):
        return "financial_planning", "financial_planning"

    if any(p in q for p in [
        "calculate mortgage",
        "future value",
        "convert",
        "compound interest",
        "if i invest",
        "how much if",
        "what will i have",
        "emi",
        "loan",
        "calculator",
    ]):
        return "financial_calculator", "financial_calculator"

    if any(p in q for p in [
        "downside risk",
        "beta",
        "max drawdown",
        "stress test",
        "risk",
        "volatility",
        "drawdown",
        "exposed am i",
    ]):
        return "risk_assessment", "risk_assessment"

    if any(p in q for p in [
        "recommend a large cap etf",
        "which fund should i buy",
        "best low-cost world index fund",
        "recommend a dividend etf",
        "fund recommendation",
        "product recommendation",
        "best etf",
    ]):
        return "product_recommendation", "product_recommendation"

    if any(p in q for p in [
        "where will",
        "predict",
        "forecast",
        "in 6 months",
        "in 5 years",
        "next year",
        "future outlook",
        "what happens if",
    ]):
        return "predictive_analysis", "predictive_analysis"

    if any(p in q for p in [
        "price of",
        "tell me about",
        "news on",
        "markets today",
        "top gainers",
        "gold price",
        "eur/usd",
        "ftse",
        "nikkei",
        "apple",
        "nvidia",
        "tesla",
        "microsoft",
        "hsbc",
        "barclays",
        "asml",
        "toyota",
    ]):
        return "market_research", "market_research"

    if entities.tickers and len(q.split()) <= 3:
        return "market_research", "market_research"

    return "general_query", "general_query"


class ClassifierService:
    def __init__(self, llm_client=None):
        self.llm_client = llm_client

    def classify(self, query: str, prior_turns: list[str]) -> ClassificationResult:
        text = " ".join(prior_turns + [query])
        entities = extract_entities(text)
        intent, agent = route_query(text, entities)
        return ClassificationResult(
            intent=intent,
            target_agent=agent,
            extracted_entities=entities,
            safety_verdict="unknown",
        )


def classify(query: str, llm=None, prior_turns: list[str] | None = None):
    return ClassifierService().classify(query, prior_turns or [])