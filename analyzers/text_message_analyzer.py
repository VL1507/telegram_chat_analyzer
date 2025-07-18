from typing import Any

import matplotlib.pyplot as plt
import numpy as np

from analyzers.base_analyzer import BaseAnalyzer


class TextMessageAnalyzer(BaseAnalyzer):
    def analyze(self) -> None:
        self.stats["activity_by_message_length_base64"] = (
            self._get_activity_by_message_length_base64()
        )

    def _get_activity_by_message_length_base64(self) -> str:
        heatmap_data = np.zeros((7, 24), dtype=int)

        for msg in self.chat_data["messages"]:
            msg: dict[str, Any]
            if msg["type"] == "message":
                if "text" in msg:
                    dt = self._to_date(msg["date"])
                    day_of_week = dt.weekday()
                    hour = dt.hour
                    heatmap_data[day_of_week, hour] += len(msg["text"])

        heatmap_data = heatmap_data / heatmap_data.max()

        plt.figure(figsize=(12, 6)) # type: ignore
        plt.imshow(heatmap_data, cmap="viridis", aspect="auto") # type: ignore
        plt.colorbar(label="Относительная активность") # type: ignore
        plt.xticks(np.arange(24), labels=np.arange(24)) # type: ignore
        plt.yticks(np.arange(7), labels=["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]) # type: ignore
        plt.xlabel("Час дня") # type: ignore
        plt.ylabel("День недели") # type: ignore
        plt.title("Активность сообщений по времени") # type: ignore

        img_base64 = self._save_plot_to_base64()
        plt.close()

        activity_by_message_length_base64 = f"data:image/png;base64,{img_base64}"

        return activity_by_message_length_base64
