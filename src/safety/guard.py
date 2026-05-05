# # from src.models.responses import SafetyResult
# # from src.safety.patterns import BLOCK_PATTERNS, EDUCATIONAL_HINTS, REFUSAL_MESSAGES


# # class SafetyGuard:
# #     def evaluate(self, text: str) -> SafetyResult:
# #         normalized = " ".join(text.lower().split())
# #         educational = any(hint in normalized for hint in EDUCATIONAL_HINTS)

# #         for category, patterns in BLOCK_PATTERNS.items():
# #             if any(pattern in normalized for pattern in patterns):
# #                 if educational:
# #                     return SafetyResult(allowed=True)
# #                 return SafetyResult(
# #                     allowed=False,
# #                     category=category,
# #                     message=REFUSAL_MESSAGES[category],
# #                 )

# #         return SafetyResult(allowed=True)


# import re
# from src.models.responses import SafetyResult

# CATEGORY_PATTERNS = {
#     "insider_trading": [
#         r"\binsider trading\b",
#         r"\binside information\b",
#         r"\binsider information\b",
#         r"\bmaterial non[- ]public\b",
#         r"\bmnpi\b",
#         r"\btrade before earnings\b",
#         r"\buse a leak to trade\b",
#         r"\bnon public information\b",
#     ],
#     "market_manipulation": [
#         r"\bpump and dump\b",
#         r"\bmanipulate (the )?price\b",
#         r"\bspoof(ing)?\b",
#         r"\bwash trade\b",
#         r"\bfake volume\b",
#         r"\brun up the stock\b",
#         r"\bcoordinate buying to move\b",
#     ],
#     "money_laundering": [
#         r"\blaunder money\b",
#         r"\bclean dirty money\b",
#         r"\bhide illicit funds\b",
#         r"\bevade aml\b",
#         r"\bavoid aml\b",
#         r"\bwash cash\b",
#         r"\bdisguise source of funds\b",
#     ],
#     "guaranteed_returns": [
#         r"\bguaranteed return\b",
#         r"\bguaranteed profit\b",
#         r"\brisk[- ]free profit\b",
#         r"\bpromise returns\b",
#         r"\bno[- ]risk return\b",
#     ],
#     "reckless_advice": [
#         r"\ball in on\b",
#         r"\bmax leverage\b",
#         r"\b100x leverage\b",
#         r"\bbet my life savings\b",
#         r"\bborrow to invest everything\b",
#         r"\bput everything into one stock\b",
#         r"\bleverage to the max\b",
#     ],
# }

# REFUSAL_MESSAGES = {
#     "insider_trading": "I can't help with trading on non-public information or similar unlawful conduct. I can explain market-abuse rules and legal investing alternatives.",
#     "market_manipulation": "I can't help manipulate markets, create false signals, or coordinate deceptive trading activity. I can explain legal market structure and compliance risks.",
#     "money_laundering": "I can't assist with concealing funds, evading AML controls, or disguising the source of money. I can explain AML requirements and legitimate compliance practices.",
#     "guaranteed_returns": "I can't support claims of guaranteed investment returns. I can help evaluate risk, diversification, and realistic return expectations.",
#     "reckless_advice": "I can't support reckless investing such as extreme leverage, concentrated all-in positions, or advice detached from risk controls. I can help build a safer plan.",
# }

# EDUCATIONAL_HINTS = [
#     "what is",
#     "explain",
#     "for learning",
#     "educational",
#     "teach me",
#     "how does",
#     "why is",
#     "risks of",
#     "tell me about",
# ]


# class SafetyGuard:
#     def evaluate(self, text: str) -> SafetyResult:
#         normalized = " ".join(text.lower().split())
#         educational = any(hint in normalized for hint in EDUCATIONAL_HINTS)

#         for category, patterns in CATEGORY_PATTERNS.items():
#             for pattern in patterns:
#                 if re.search(pattern, normalized):
#                     if educational:
#                         return SafetyResult(allowed=True)
#                     return SafetyResult(
#                         allowed=False,
#                         category=category,
#                         message=REFUSAL_MESSAGES[category],
#                     )
#         return SafetyResult(allowed=True)


# _guard = SafetyGuard()


# def check(query: str) -> SafetyResult:
#     return _guard.evaluate(query)













# import re
# from src.models.responses import SafetyResult

# CATEGORY_PATTERNS = {
#     "insider_trading": [
#         r"\binsider trading\b",
#         r"\binside information\b",
#         r"\binsider information\b",
#         r"\bmaterial non[- ]public information\b",
#         r"\bmaterial non[- ]public\b",
#         r"\bmnpi\b",
#         r"\bnon[- ]public information\b",
#         r"\btrade on inside info\b",
#         r"\btrade before earnings\b",
#         r"\buse a leak to trade\b",
#         r"\bsecret earnings\b",
#     ],
#     "market_manipulation": [
#         r"\bpump and dump\b",
#         r"\bpump this stock\b",
#         r"\bmanipulate (the )?(stock|price|market)\b",
#         r"\bspoof(ing)?\b",
#         r"\bwash trade\b",
#         r"\bfake volume\b",
#         r"\bmove the price\b",
#         r"\brun up the stock\b",
#         r"\bcoordinate buying\b",
#     ],
#     "money_laundering": [
#         r"\blaunder money\b",
#         r"\bclean dirty money\b",
#         r"\bhide illicit funds\b",
#         r"\bevade aml\b",
#         r"\bavoid aml\b",
#         r"\bwash cash\b",
#         r"\bdisguise source of funds\b",
#         r"\bmove dirty money\b",
#     ],
#     "guaranteed_returns": [
#         r"\bguaranteed return\b",
#         r"\bguaranteed profit\b",
#         r"\brisk[- ]free profit\b",
#         r"\bno[- ]risk return\b",
#         r"\bpromise returns\b",
#         r"\bcertain profit\b",
#         r"\bcan.t lose\b",
#     ],
#     "reckless_advice": [
#         r"\ball in on\b",
#         r"\bmax leverage\b",
#         r"\b100x leverage\b",
#         r"\bbet my life savings\b",
#         r"\bborrow to invest everything\b",
#         r"\bput everything into one stock\b",
#         r"\bleverage to the max\b",
#         r"\byolo\b",
#         r"\bmortgage .* invest\b",
#     ],
# }

# REFUSAL_MESSAGES = {
#     "insider_trading": "I can't help with trading on non-public information or similar unlawful conduct. I can explain market-abuse rules and legal investing alternatives.",
#     "market_manipulation": "I can't help manipulate markets, create false signals, or coordinate deceptive trading activity. I can explain legal market structure and compliance risks.",
#     "money_laundering": "I can't assist with concealing funds, evading AML controls, or disguising the source of money. I can explain AML requirements and legitimate compliance practices.",
#     "guaranteed_returns": "I can't support claims of guaranteed investment returns. I can help evaluate risk, diversification, and realistic return expectations.",
#     "reckless_advice": "I can't support reckless investing such as extreme leverage, concentrated all-in positions, or advice detached from risk controls. I can help build a safer plan.",
# }

# EDUCATIONAL_HINTS = [
#     "what is",
#     "explain",
#     "for learning",
#     "educational",
#     "teach me",
#     "how does",
#     "why is",
#     "risks of",
#     "tell me about",
#     "is it illegal",
#     "why is this illegal",
#     "for a school project",
# ]


# class SafetyGuard:
#     def evaluate(self, text: str) -> SafetyResult:
#         normalized = " ".join(text.lower().split())
#         educational = any(hint in normalized for hint in EDUCATIONAL_HINTS)

#         for category, patterns in CATEGORY_PATTERNS.items():
#             if any(re.search(pattern, normalized) for pattern in patterns):
#                 if educational:
#                     return SafetyResult(allowed=True)
#                 return SafetyResult(
#                     allowed=False,
#                     category=category,
#                     message=REFUSAL_MESSAGES[category],
#                 )

#         return SafetyResult(allowed=True)


# _guard = SafetyGuard()


# def check(query: str) -> SafetyResult:
#     return _guard.evaluate(query)













import re
from src.models.responses import SafetyResult

RULES = {
    "insider_trading": [
        r"unannounced acquisition",
        r"confidential merger",
        r"load up before the call",
        r"know about .*buy shares",
        r"earnings before tomorrow",
        r"non-public information",
        r"material non-public information",
        r"inside information",
        r"insider trading",
        r"insider dealing",
        r"front[- ]running",
    ],
    "market_manipulation": [
        r"pump up the price",
        r"pump and dump",
        r"coordinated buying",
        r"move this stock",
        r"wash trade",
        r"spoofing",
        r"layering",
        r"manipulation",
    ],
    "money_laundering": [
        r"move .*cash through stock trading",
        r"avoid the 10k reporting threshold",
        r"structure deposits",
        r"layer my trades",
        r"hide trading profits",
        r"money laundering",
        r"aml",
        r"source of these funds",
    ],
    "guaranteed_returns": [
        r"guarantee me .* returns",
        r"promise me .* double",
        r"100% certain to go up",
        r"foolproof way",
        r"guaranteed-return",
        r"certain profit",
        r"risk[- ]free profit",
    ],
    "reckless_advice": [
        r"all my retirement savings in crypto",
        r"take a margin loan",
        r"entire emergency fund into options",
        r"mortgage my house",
        r"borrow to invest everything",
        r"all in on",
    ],
    "sanctions_evasion": [
        r"bypass ofac",
        r"sanctioned russian company",
        r"shell company",
        r"without it being traced",
        r"sanctions evasion",
        r"screen for them",
    ],
    "fraud": [
        r"fake contract note",
        r"claim losses",
        r"fake contract",
        r"forg[e]? losses",
    ],
}

MESSAGES = {
    "insider_trading": "I can’t help with insider trading or trading on non-public information. I can explain legal market-abuse rules instead.",
    "market_manipulation": "I can’t help manipulate prices or coordinate deceptive trading. I can explain why those schemes are illegal.",
    "money_laundering": "I can’t help conceal money, evade reporting rules, or structure transactions to hide funds. I can explain AML rules instead.",
    "guaranteed_returns": "I can’t help promise guaranteed returns or foolproof profits. I can help discuss risk and realistic expectations.",
    "reckless_advice": "I can’t support reckless investing such as mortgaging property, max leverage, or gambling an emergency fund. I can help build a safer plan.",
    "sanctions_evasion": "I can’t help bypass sanctions or hide dealings with sanctioned entities. I can explain compliance obligations instead.",
    "fraud": "I can’t help create fake documents or commit fraud. I can explain legitimate recordkeeping and compliance.",
}

EDU_ALLOW = [
    "what is", "explain", "how does", "why is", "what are", "difference between",
    "under the sec", "under fca", "what are the penalties", "why are", "describe"
]

class SafetyGuard:
    def evaluate(self, text: str) -> SafetyResult:
        q = " ".join(text.lower().split())
        is_educational = any(h in q for h in EDU_ALLOW)

        for category, patterns in RULES.items():
            if any(re.search(p, q) for p in patterns):
                if is_educational:
                    return SafetyResult(allowed=True)
                return SafetyResult(allowed=False, category=category, message=MESSAGES[category])

        return SafetyResult(allowed=True)

_guard = SafetyGuard()

def check(query: str) -> SafetyResult:
    return _guard.evaluate(query)