from __future__ import annotations

from typing import Protocol
from openai import OpenAI

from src.classifier.prompts import SYSTEM_PROMPT
from src.config import settings
from src.models.classification import ClassificationResult


class LLMClient(Protocol):
    def classify(self, user_query: str, conversation_context: list[str]) -> ClassificationResult:
        ...


class OpenAIClassifierClient:
    def __init__(self) -> None:
        self.client = OpenAI(api_key=settings.openai_api_key) if settings.openai_api_key else None

    def classify(self, user_query: str, conversation_context: list[str]) -> ClassificationResult:
        if not self.client:
            raise RuntimeError("OPENAI_API_KEY not configured")

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"Conversation history: {conversation_context}\nCurrent query: {user_query}",
            },
        ]

        response = self.client.responses.parse(
            model=settings.openai_model,
            input=messages,
            text_format=ClassificationResult,
        )
        return response.output_parsed