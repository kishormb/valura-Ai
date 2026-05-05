[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/SHM9MYZJ)
# Valura AI — Team Lead Project Assignment

You have been given access to this repository as part of the Valura AI team lead hiring process.

**Read [`ASSIGNMENT.md`](ASSIGNMENT.md) in full before writing a single line of code.**

---

## What you're building

An AI agent ecosystem that helps a novice investor **build, monitor, grow, and protect** their portfolio. See [`ASSIGNMENT.md`](ASSIGNMENT.md) for the full mission, scope, and constraints.

---

## Setup

**Requirements:** Python 3.11+, an OpenAI API key.

**Persistence is your choice.** Postgres, SQLite, or in-memory — pick one and defend it in your README. `DATABASE_URL` in `.env.example` is optional.

**Streaming is required.** SSE only. Use `sse-starlette`, FastAPI's `StreamingResponse`, or roll your own — your call.

```bash
git clone <your-classroom-repo-url>
cd <repo-name>

python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows

pip install -r requirements.txt

cp .env.example .env
# Fill in OPENAI_API_KEY
```

Use `gpt-4o-mini` while developing to keep costs down. Evaluation runs against `gpt-4.1`.

---

## Running Tests

```bash
pytest tests/ -v
```

Tests must pass without an `OPENAI_API_KEY` set — mock the LLM. We will run `pytest tests/ -v` on your repo.

---

## Repository Structure

When you submit, your repository must contain:

```
README.md   ← overwrite this with your own (setup, decisions, library choices, video link)
src/        ← all code
tests/      ← all tests, must pass with pytest
```

`fixtures/`, `pytest.ini`, `requirements.txt`, `.env.example`, and `.github/` are part of the scaffold — leave them in place. Do not delete `ASSIGNMENT.md`.

---

## Submission

- Push commits **throughout** your work — we read the git log
- Your `README.md` must:
  - Explain how to run your code
  - List every required environment variable
  - Document the non-obvious decisions you made
  - Link your defence video (≤ 10 min — see `ASSIGNMENT.md`)
- Deadline: **3 days** from the date you accepted this assignment
- Defence video: due within **24 hours** of your final commit

---

## Environment

You self-host everything. We do not provide credentials. See `.env.example` for the variables you'll need.



## The updated readme file after updathinh the code by compliting the assignment 
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