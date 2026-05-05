from src.api.sse import chunk_event, done_event, error_event, meta_event, result_event


class Orchestrator:
    def __init__(self, safety_guard, classifier_service, agent_router, session_store, user_loader):
        self.safety_guard = safety_guard
        self.classifier_service = classifier_service
        self.agent_router = agent_router
        self.session_store = session_store
        self.user_loader = user_loader

    async def stream(self, session_id: str, user_id: str, query: str):
        try:
            safety = self.safety_guard.evaluate(query)
            if not safety.allowed:
                yield meta_event({"blocked": True, "category": safety.category})
                yield chunk_event(safety.message)
                yield done_event()
                return

            prior_turns = self.session_store.get_turns(session_id)
            classification = self.classifier_service.classify(query, prior_turns)
            user_profile = self.user_loader(user_id)
            result = self.agent_router.dispatch(classification, user_profile)

            self.session_store.append_user_turn(session_id, query)

            yield meta_event(
                {
                    "blocked": False,
                    "intent": classification.intent,
                    "target_agent": classification.target_agent,
                    "safety_verdict": classification.safety_verdict,
                }
            )

            for line in self._summarize(result):
                yield chunk_event(line)

            yield result_event(result.model_dump())
            yield done_event()

        except Exception as exc:
            yield error_event("pipeline_error", str(exc))
            yield done_event()

    def _summarize(self, result):
        if hasattr(result, "observations"):
            return [obs.text for obs in result.observations] or ["Analysis complete."]
        if hasattr(result, "message"):
            return [result.message]
        return ["Request processed."]