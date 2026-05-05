from src.utils.sse import sse_event


def meta_event(payload: dict):
    return sse_event("meta", payload)


def chunk_event(text: str):
    return sse_event("chunk", {"text": text})


def result_event(payload: dict):
    return sse_event("result", payload)


def error_event(code: str, message: str):
    return sse_event("error", {"code": code, "message": message})


def done_event():
    return sse_event("done", {"ok": True})