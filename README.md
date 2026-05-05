
# Valura AI Microservice

## Overview
Valura AI Microservice is a FastAPI-based AI routing layer for financial queries. It classifies incoming user questions, applies a local safety guard, routes the request to the correct specialist agent, and streams the response back over SSE.

## Architecture
Show a quick diagram or explain in words:
POST /query
   ↓
Safety Guard (rule-based, no LLM)
   ↓
Intent Classifier (LLM / deterministic fallback)
   ↓
Router
   ↓
Agent (Portfolio Health or Stub)
   ↓
SSE Streaming Response

Request flow:
1. Safety guard runs first.
2. Intent classifier extracts intent, entities, and target agent.
3. Router dispatches to the appropriate agent.
4. Portfolio Health is fully implemented.
5. Other agents return structured stub responses.
6. The response streams to the client using Server-Sent Events.

## Safety Guard
The safety guard is local, fast, and does not call any model. It blocks harmful requests such as insider trading, market manipulation, money laundering, guaranteed-return claims, and reckless advice. Educational questions are allowed where possible, but some over-blocking is an accepted tradeoff.

## Intent Classifier
The classifier returns:
- intent
- extracted entities
- target agent
- informational safety verdict

It also handles follow-up context by considering prior turns. The implementation is test-friendly and works without an API key in CI.

## Portfolio Health Agent
This is the fully implemented agent. It analyzes concentration risk, performance, benchmark comparison, and actionable observations. It handles empty portfolios gracefully and returns BUILD-oriented advice for users who have no holdings yet.

## Stub Agents
All other agents named in the assignment are routed correctly, but if they are not implemented they return a structured `not_implemented` response instead of crashing.

## HTTP Layer and SSE
The application exposes `POST /query` and streams results using SSE events:
- `meta`
- `chunk`
- `result`
- `error`
- `done`

## Frontend Demo
A minimal HTML + vanilla JavaScript page is included to demonstrate streaming responses from `POST /query`.

## Setup
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Environment Variables
Required and optional variables are documented in `.env.example`.

## Running Locally
```bash
uvicorn src.main:app --reload
```

## Testing
```bash
pytest tests/ -v
```
Tests are designed to pass without `OPENAI_API_KEY`.

## Design Decisions
- FastAPI for async API and SSE support.
- In-memory session storage for simplicity and reliability in the assignment context.
- Rule-based safety guard for speed and deterministic behavior.
- One classifier step to keep latency and cost low.
- `yfinance` or equivalent market-data source for non-hardcoded external market info.

## Performance and Cost
The development model is `gpt-4o-mini`. The evaluation target is `gpt-4.1`. The design keeps one LLM call per classification and avoids unnecessary calls in the safety layer.

## Limitations
- Only Portfolio Health is fully implemented.
- Other agents are stubs.
- Session persistence is in-memory for this submission.

## Demo Video
Unlisted YouTube link: <ADD_LINK_HERE>