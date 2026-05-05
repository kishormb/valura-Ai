from collections import defaultdict


class InMemorySessionStore:
    def __init__(self) -> None:
        self._sessions: dict[str, list[str]] = defaultdict(list)

    def get_turns(self, session_id: str) -> list[str]:
        return list(self._sessions.get(session_id, []))

    def append_user_turn(self, session_id: str, message: str) -> None:
        self._sessions[session_id].append(message)