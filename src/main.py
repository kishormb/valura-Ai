# # from fastapi import FastAPI
# # from src.api.routes import router

# # app = FastAPI(title="Valura AI Microservice", version="1.0.0")
# # app.include_router(router)


# # @app.get("/healthz")
# # def healthz():
# #     return {"status": "ok"}

# from fastapi import FastAPI
# from fastapi.responses import RedirectResponse

# from src.api.routes import router

# app = FastAPI(title="Valura AI Microservice", version="1.0.0")
# app.include_router(router)


# @app.get("/", include_in_schema=False)
# def root():
#     return RedirectResponse(url="/docs")


# @app.get("/healthz")
# def healthz():
#     return {"status": "ok"}











# from fastapi import FastAPI
# from fastapi.responses import RedirectResponse

# from src.api.routes import router

# app = FastAPI(title="Valura AI Microservice", version="1.0.0")
# app.include_router(router)


# @app.get("/", include_in_schema=False)
# def root():
#     return RedirectResponse(url="/docs")


# @app.get("/healthz")
# def healthz():
#     return {"status": "ok"}













# from fastapi import FastAPI
# from fastapi.responses import HTMLResponse

# app = FastAPI(title="Valura AI Microservice", version="1.0.0")

# @app.get("/", response_class=HTMLResponse)
# def root():
#     return """
#     <html>
#       <head><title>Valura AI Microservice</title></head>
#       <body style="font-family: sans-serif; padding: 2rem;">
#         <h1>Valura AI Microservice</h1>
#         <p>Service is running.</p>
#         <ul>
#           <li><a href="/docs">API docs</a></li>
#           <li><a href="/healthz">Health check</a></li>
#         </ul>
#       </body>
#     </html>
#     """






# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse, StreamingResponse
# import asyncio
# import json
# from typing import AsyncGenerator

# # 🔹 Import your real modules here
# # from src.safety.guard import safety_guard
# # from src.classifier.classifier import classify
# # from src.router.router import route_to_agent

# app = FastAPI(title="Valura AI Microservice", version="1.0.0")


# # --------------------------------------------------
# # Root (UI placeholder)
# # --------------------------------------------------
# @app.get("/", response_class=HTMLResponse)
# def root():
#     return """
#     <html>
#       <head><title>Valura AI Microservice</title></head>
#       <body style="font-family: sans-serif; padding: 2rem;">
#         <h1>Valura AI Microservice</h1>
#         <p>Service is running.</p>
#         <ul>
#           <li><a href="/docs">API docs</a></li>
#           <li><a href="/healthz">Health check</a></li>
#         </ul>
#       </body>
#     </html>
#     """


# # --------------------------------------------------
# # Health check
# # --------------------------------------------------
# @app.get("/healthz")
# def health():
#     return {"status": "ok"}


# # --------------------------------------------------
# # Helper: format SSE event
# # --------------------------------------------------
# def sse_event(event: str, data: dict | str) -> str:
#     payload = data if isinstance(data, str) else json.dumps(data)
#     return f"event: {event}\ndata: {payload}\n\n"


# # --------------------------------------------------
# # MAIN ENDPOINT (REQUIRED)
# # --------------------------------------------------
# @app.post("/query")
# async def query(request: Request):
#     try:
#         body = await request.json()
#         user_query = body.get("query", "")

#         async def event_stream() -> AsyncGenerator[str, None]:
#             try:
#                 # ------------------------------------------
#                 # 1. META EVENT
#                 # ------------------------------------------
#                 yield sse_event("meta", {"query": user_query})

#                 # ------------------------------------------
#                 # 2. SAFETY GUARD (LOCAL, NO LLM)
#                 # ------------------------------------------
#                 # Replace with your real safety logic
#                 if "insider trading" in user_query.lower():
#                     yield sse_event("error", {
#                         "type": "safety_violation",
#                         "message": "I can't assist with insider trading or illegal activities."
#                     })
#                     return

#                 # ------------------------------------------
#                 # 3. CLASSIFIER (LLM - MOCK SAFE FALLBACK)
#                 # ------------------------------------------
#                 # Replace with your real classifier
#                 classification = {
#                     "intent": "portfolio_health",
#                     "agent": "portfolio_health",
#                     "entities": {}
#                 }

#                 yield sse_event("meta", {"classification": classification})

#                 # ------------------------------------------
#                 # 4. ROUTING
#                 # ------------------------------------------
#                 agent = classification["agent"]

#                 # ------------------------------------------
#                 # 5. AGENT EXECUTION
#                 # ------------------------------------------
#                 if agent == "portfolio_health":
#                     # Replace with your real agent
#                     chunks = [
#                         "Analyzing your portfolio...",
#                         "Your portfolio appears moderately diversified.",
#                         "No extreme concentration risks detected.",
#                         "You are slightly outperforming your benchmark."
#                     ]

#                     for chunk in chunks:
#                         await asyncio.sleep(0.4)
#                         yield sse_event("chunk", chunk)

#                     # structured summary (optional final chunk)
#                     result = {
#                         "concentration_risk": {"flag": "medium"},
#                         "performance": {"total_return_pct": 12.4},
#                         "observations": [
#                             {"severity": "info", "text": "Diversification is reasonable."}
#                         ],
#                         "disclaimer": "This is not investment advice."
#                     }

#                     yield sse_event("meta", {"result": result})

#                 else:
#                     # ------------------------------------------
#                     # STUB AGENTS (REQUIRED BY ASSIGNMENT)
#                     # ------------------------------------------
#                     stub = {
#                         "agent": agent,
#                         "message": f"{agent} agent is not implemented in this build.",
#                         "entities": classification.get("entities", {})
#                     }

#                     yield sse_event("chunk", json.dumps(stub))

#                 # ------------------------------------------
#                 # 6. DONE
#                 # ------------------------------------------
#                 yield sse_event("done", {})

#             except Exception as e:
#                 yield sse_event("error", {"message": str(e)})

#         return StreamingResponse(event_stream(), media_type="text/event-stream")

#     except Exception as e:
#         return {"error": str(e)}
































# from pathlib import Path
# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse, StreamingResponse, JSONResponse

# app = FastAPI(title="Valura AI Microservice", version="1.0.0")

# def sse_event(event: str, data) -> str:
#     import json
#     payload = data if isinstance(data, str) else json.dumps(data)
#     return f"event: {event}\ndata: {payload}\n\n"

# @app.get("/", response_class=HTMLResponse)
# def root():
#     html_path = Path("output/index.html")
#     if html_path.exists():
#         return html_path.read_text(encoding="utf-8")
#     return "<h1>Valura AI Microservice</h1><p>Service is running.</p>"

# @app.get("/healthz")
# def health():
#     return {"status": "ok"}

# @app.post("/query")
# async def query(request: Request):
#     body = await request.json()
#     user_query = body.get("query", "")
#     user_id = body.get("user_id", "usr_004")
#     session_id = body.get("session_id", "session")

#     async def event_stream():
#         try:
#             yield sse_event("meta", {"session_id": session_id, "user_id": user_id})

#             from src.safety.guard import check
#             verdict = check(user_query)
#             if verdict.blocked:
#                 yield sse_event("error", {
#                     "type": "safety_violation",
#                     "message": verdict.message or "Blocked by safety guard"
#                 })
#                 yield sse_event("done", {"ok": True})
#                 return

#             from src.classifier.service import classify
#             classification = classify(user_query)
#             yield sse_event("meta", {
#                 "classification": {
#                     "intent": classification.intent,
#                     "agent": classification.agent,
#                     "entities": classification.entities,
#                     "safety_verdict": classification.safety_verdict,
#                 }
#             })

#             if classification.agent == "portfolio_health":
#                 from src.dependencies import load_user_profile
#                 from src.agents.portfolio_health import run
#                 user = load_user_profile(user_id)
#                 result = run(user)
#                 for chunk in [
#                     "Analyzing your portfolio...",
#                     "Building concentration and performance summary...",
#                     "Preparing final result..."
#                 ]:
#                     yield sse_event("chunk", {"text": chunk})
#                 yield sse_event("result", result)
#             else:
#                 yield sse_event("chunk", {"text": f"{classification.agent} agent is not implemented in this build."})
#                 yield sse_event("result", {
#                     "status": "not_implemented",
#                     "agent": classification.agent,
#                     "intent": classification.intent,
#                     "entities": classification.entities,
#                 })

#             yield sse_event("done", {"ok": True})

#         except Exception as e:
#             yield sse_event("error", {"message": str(e)})
#             yield sse_event("done", {"ok": False})

#     return StreamingResponse(event_stream(), media_type="text/event-stream")














from pathlib import Path
import json

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse

app = FastAPI(title="Valura AI Microservice", version="1.0.0")


def sse_event(event: str, data) -> str:
    payload = data if isinstance(data, str) else json.dumps(data)
    return f"event: {event}\ndata: {payload}\n\n"


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def root():
    html_path = Path("output/index.html")
    if html_path.exists():
        return html_path.read_text(encoding="utf-8")
    return """
    <html>
      <head><title>Valura AI Microservice</title></head>
      <body style="font-family: Arial, sans-serif; padding: 2rem;">
        <h1>Valura AI Microservice</h1>
        <p>Service is running.</p>
        <ul>
          <li><a href="/docs">API docs</a></li>
          <li><a href="/healthz">Health check</a></li>
        </ul>
      </body>
    </html>
    """


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.post("/query")
async def query(request: Request):
    body = await request.json()
    user_query = body.get("query", "")
    user_id = body.get("user_id", "usr_004")
    session_id = body.get("session_id", "session")

    async def event_stream():
        try:
            yield sse_event("meta", {"session_id": session_id, "user_id": user_id})

            from src.safety.guard import check
            verdict = check(user_query)
            if verdict.blocked:
                yield sse_event(
                    "error",
                    {
                        "type": "safety_violation",
                        "message": verdict.message or "Blocked by safety guard",
                    },
                )
                yield sse_event("done", {"ok": True})
                return

            from src.classifier.service import classify
            classification = classify(user_query)

            yield sse_event(
                "meta",
                {
                    "classification": {
                        "intent": classification.intent,
                        "agent": classification.agent,
                        "entities": classification.entities,
                        "safety_verdict": classification.safety_verdict,
                    }
                },
            )

            if classification.agent == "portfolio_health":
                from src.dependencies import load_user_profile
                from src.agents.portfolio_health import run

                user = load_user_profile(user_id)

                for chunk in [
                    "Analyzing your portfolio...",
                    "Building concentration and performance summary...",
                    "Preparing final result...",
                ]:
                    yield sse_event("chunk", {"text": chunk})

                result = run(user)
                yield sse_event("result", result)

            else:
                yield sse_event(
                    "chunk",
                    {"text": f"{classification.agent} agent is not implemented in this build."},
                )
                yield sse_event(
                    "result",
                    {
                        "status": "not_implemented",
                        "agent": classification.agent,
                        "intent": classification.intent,
                        "entities": classification.entities,
                    },
                )

            yield sse_event("done", {"ok": True})

        except Exception as exc:
            yield sse_event("error", {"message": str(exc)})
            yield sse_event("done", {"ok": False})

    return StreamingResponse(event_stream(), media_type="text/event-stream")