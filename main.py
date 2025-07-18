from telegram_chat_analyzer import TelegramChatAnalyzer


def main():
    file_path = r"C:\Users\vovam\prog\telegram_chat_analyzer\result.json"
    # chat_id = 2081431134
    chat_id = 1877558567

    tca = TelegramChatAnalyzer(
        file_path=file_path,
        chat_id=chat_id,
    )

    tca.analyze_and_generate_report()


if __name__ == "__main__":
    main()
