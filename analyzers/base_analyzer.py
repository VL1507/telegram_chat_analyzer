import base64
from abc import ABC, abstractmethod
from datetime import datetime
from io import BytesIO
from typing import Any

import matplotlib.pyplot as plt


class BaseAnalyzer(ABC):
    def __init__(self, chat_data: dict[str, Any]) -> None:
        super().__init__()
        self.chat_data = chat_data
        self.stats: dict[str, Any] = dict()

    @abstractmethod
    def analyze(self) -> None: ...

    def get_stats(self) -> dict[str, Any]:
        return self.stats

    def _to_date(
        self, date_string: str, format_: str = "%Y-%m-%dT%H:%M:%S"
    ) -> datetime:
        return datetime.strptime(date_string, format_)

    def _save_plot_to_base64(self):
        buf = BytesIO()
        plt.savefig(buf, format="png", bbox_inches="tight", dpi=100) # type: ignore
        buf.seek(0)
        return base64.b64encode(buf.read()).decode("utf-8")
