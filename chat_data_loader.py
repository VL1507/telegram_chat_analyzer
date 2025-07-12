import json
from typing import Any


class ChatDataLoader:
    def __init__(self, file_path: str, chat_id: int) -> None:
        self.file_path = file_path
        self.chat_id = chat_id

    def load_data(self) -> dict[str, Any]:
        with open(self.file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        chats_list = data["chats"]["list"]

        for chat in chats_list:
            if chat["id"] == self.chat_id:
                return chat

        raise ValueError(f"Chat with ID {self.chat_id} not found")
