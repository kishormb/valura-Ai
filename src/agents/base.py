from typing import Protocol


class Agent(Protocol):
    def run(self, *args, **kwargs):
        ...