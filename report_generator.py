from typing import Any

from jinja2 import Environment, FileSystemLoader


class ReportGenerator:
    def __init__(self, stats: dict[str, Any], output_path: str = "report.html") -> None:
        self.stats = stats
        self.output_path = output_path
        self.template_path = "report_template.html"

    def generate_report(self) -> None:
        file_loader = FileSystemLoader(".")
        env = Environment(loader=file_loader)
        template = env.get_template(self.template_path)
        output = template.render(stats=self.stats)
        with open(self.output_path, "w") as f:
            f.write(output)
