from pathlib import Path
import markdown
from html2image import Html2Image
from tools.report_style import get_styled_html


def convert_md_to_image(md_path: str, output_path: str):
    md_text = Path(md_path).read_text(encoding="utf-8")

    html = markdown.markdown(md_text, extensions=["tables"])
    styled_html = get_styled_html(html)

    temp_html = Path(md_path).with_suffix(".html")
    temp_html.write_text(styled_html, encoding="utf-8")

    hti = Html2Image(output_path=Path(output_path).parent)

    hti.screenshot(
        html_file=str(temp_html),
        save_as=Path(output_path).name,
        size=(1200, 1800)   # 🔥 HIGH RESOLUTION
    )

    return output_path