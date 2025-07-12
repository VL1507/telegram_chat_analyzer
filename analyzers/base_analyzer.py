from abc import ABC, abstractmethod
from typing import Any


class BaseAnalyzer(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.stats: dict[str, Any] = dict()

    @abstractmethod
    def analyze(self) -> None: ...

    def get_stats(self) -> dict[str, Any]:
        return self.stats
