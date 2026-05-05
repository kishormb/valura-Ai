def normalize_ticker(value: str) -> str:
    value = value.strip().upper()
    return value.split(".")[0]