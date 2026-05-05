import json


def sse_event(event: str, data):
    return {"event": event, "data": json.dumps(data, ensure_ascii=False)}