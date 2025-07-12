from typing import Any

import jinja2

# from jinja2 import Environment, FileSystemLoader


class ReportGenerator:
    def __init__(
        self,
        stats: dict[str, Any],
        output_path: str = "report.html",
        template_path: str | None = None,
    ) -> None:
        self.stats = stats
        self.output_path = output_path

        if template_path is None:
            self.template_path = "report_template.html"
        else:
            self.template_path = template_path

    def generate(self) -> None:
        with open(self.template_path, "r", encoding="utf-8") as f:
            template = jinja2.Template(f.read())
        html = template.render(self.stats)

        with open(self.output_path, "w", encoding="utf-8") as f:
            f.write(html)

    # def generate(self) -> None:
    #     # file_loader = FileSystemLoader(".")
    #     # env = Environment(loader=file_loader)
    #     # env.globals.update(enumerate=enumerate)
    #     # Инициализация Jinja2 с правильными настройками кодировки
    #     env = Environment(
    #         loader=FileSystemLoader('.'),
    #         autoescape=True,
    #         trim_blocks=True,
    #         lstrip_blocks=True,
    #         keep_trailing_newline=True
    #     )

    #     # Принудительная установка кодировки
    #     # env.globals.update(encoding='utf-8')

    #     template = env.get_template(self.template_path)
    #     html = template.render(img_base64=self.stats.get("img_base64"))

    #     print(self.stats)

    #     with open(self.output_path, "w", encoding="utf-8") as f:
    #         f.write(html)
