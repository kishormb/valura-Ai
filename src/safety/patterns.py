# BLOCK_PATTERNS = {
#     "insider_trading": [
#         "inside information",
#         "insider information",
#         "material non public",
#         "mnpi",
#         "trade before earnings leak",
#     ],
#     "market_manipulation": [
#         "pump and dump",
#         "spoof the market",
#         "manipulate price",
#         "wash trade",
#         "fake volume",
#     ],
#     "money_laundering": [
#         "launder money",
#         "clean dirty money",
#         "hide illicit funds",
#         "evade aml",
#     ],
#     "guaranteed_returns": [
#         "guaranteed return",
#         "guaranteed profit",
#         "risk free 20%",
#         "no risk profit",
#     ],
#     "reckless_advice": [
#         "all in on",
#         "max leverage",
#         "100x leverage",
#         "bet my life savings",
#         "borrow to invest everything",
#     ],
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
# ]

# REFUSAL_MESSAGES = {
#     "insider_trading": "I can't help with trading on non-public information or similar unlawful conduct. I can explain market-abuse rules and legal investing alternatives.",
#     "market_manipulation": "I can't help manipulate markets, create false signals, or coordinate deceptive trading activity. I can explain legal market structure and compliance risks.",
#     "money_laundering": "I can't assist with concealing funds, evading AML controls, or disguising source of money. I can explain AML requirements and legitimate compliance practices.",
#     "guaranteed_returns": "I can't support claims of guaranteed investment returns. I can help evaluate risk, diversification, and realistic return expectations.",
#     "reckless_advice": "I can't support reckless investing such as extreme leverage, concentrated all-in positions, or advice detached from risk controls. I can help build a safer plan.",
# }





BLOCK_PATTERNS = {
    "insider_trading": [
        "inside information",
        "insider information",
        "material non public",
        "material non-public",
        "mnpi",
        "trade before earnings leak",
        "use a leak to trade",
    ],
    "market_manipulation": [
        "pump and dump",
        "spoof the market",
        "manipulate price",
        "wash trade",
        "fake volume",
        "coordinate a pump",
    ],
    "money_laundering": [
        "launder money",
        "clean dirty money",
        "hide illicit funds",
        "evade aml",
        "wash cash through",
    ],
    "guaranteed_returns": [
        "guaranteed return",
        "guaranteed profit",
        "risk free 20%",
        "no risk profit",
        "promise returns",
    ],
    "reckless_advice": [
        "all in on",
        "max leverage",
        "100x leverage",
        "bet my life savings",
        "borrow to invest everything",
        "put everything into one stock",
    ],
}

EDUCATIONAL_HINTS = [
    "what is",
    "explain",
    "for learning",
    "educational",
    "teach me",
    "how does",
    "why is",
    "risks of",
    "tell me about",
]