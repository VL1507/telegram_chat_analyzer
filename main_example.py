from telegram_chat_analyzer import TelegramChatAnalyzer


def main():
    file_path = ""
    chat_id = ...

    tca = TelegramChatAnalyzer(
        file_path=file_path,
        chat_id=chat_id,
    )

    tca.analyze_and_generate_report()


if __name__ == "__main__":
    main()
