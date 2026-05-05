from src.models.responses import StubAgentResponse


class StubAgent:
    def run(self, classification_result):
        return StubAgentResponse(
            intent=classification_result.intent,
            agent=classification_result.target_agent,
            entities=classification_result.extracted_entities.model_dump(exclude_none=True),
            message="This agent is not implemented in this build.",
        )