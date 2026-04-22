from pathlib import Path
import markdown
from tools.report_style import get_styled_html


def convert_md_to_html(md_path: str, html_path: str):
    md_text = Path(md_path).read_text(encoding="utf-8")

    html = markdown.markdown(md_text, extensions=["tables"])
    styled_html = get_styled_html(html)

    Path(html_path).write_text(styled_html, encoding="utf-8")

    return html_path