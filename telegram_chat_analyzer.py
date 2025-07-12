from analyzers.chat_analyzer import ChatAnalyzer
from chat_data_loader import ChatDataLoader
from report_generator import ReportGenerator


class TelegramChatAnalyzer:
    def __init__(
        self,
        file_path: str,
        chat_id: int,
        output_path: str = "report.html",
        template_path: str | None = None,
    ):
        self.file_path = file_path
        self.chat_id = chat_id
        self.output_path = output_path
        self.template_path = template_path

    def analyze_and_generate_report(self):
        chat_data = ChatDataLoader(self.file_path, self.chat_id).load_data()

        analyzer = ChatAnalyzer(chat_data)
        analyzer.analyze()
        stats = analyzer.get_stats()

        report = ReportGenerator(stats, self.output_path, self.template_path)
        report.generate()
