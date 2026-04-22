import pdfkit
from pathlib import Path


def convert_html_to_pdf(html_path: str, output_path: str):
    html_file = Path(html_path)

    if not html_file.exists():
        raise FileNotFoundError(f"HTML file not found: {html_path}")

    config = pdfkit.configuration(
        wkhtmltopdf=r"C:\Users\kavinduk\wkhtmltopdf\bin\wkhtmltopdf.exe"
    )

    options = {
        "enable-local-file-access": "",
        "page-size": "A4",
        "margin-top": "5mm",
        "margin-bottom": "5mm",
        "margin-left": "5mm",
        "margin-right": "5mm",
        "encoding": "UTF-8",
        "zoom": "0.85",
        "dpi": 300,
        "no-outline": None,
    }

    pdfkit.from_file(
        str(html_file),
        output_path,
        configuration=config,
        options=options
    )

    return output_path