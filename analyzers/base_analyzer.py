from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any


class BaseAnalyzer(ABC):
    def __init__(self, chat_data: dict[str, Any]) -> None:
        super().__init__()
        self.chat_data = chat_data
        self.stats: dict[str, Any] = dict()

    @abstractmethod
    def analyze(self) -> None: ...

    def get_stats(self) -> dict[str, Any]:
        return self.stats

    def _to_date(self, date_string: str, format_: str = "%Y-%m-%dT%H:%M:%S") -> datetime:
        return datetime.strptime(date_string, format_)
