from typing import Any

from analyzers.base_analyzer import BaseAnalyzer
from analyzers.text_message_analyzer import TextMessageAnalyzer


class ChatAnalyzer(BaseAnalyzer):
    def __init__(self, chat_data: dict[str, Any]) -> None:
        super().__init__(chat_data)
        self.analyzers = [
            TextMessageAnalyzer(chat_data),
        ]

    def analyze(self) -> None:
        for analyzer in self.analyzers:
            analyzer.analyze()
            self.stats.update(analyzer.get_stats())
