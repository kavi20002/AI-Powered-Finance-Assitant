def get_styled_html(content: str) -> str:
    return f"""
    <html>
    <head>
        <meta charset="UTF-8">

        <style>
            body {{
                font-family: 'Segoe UI', sans-serif;
                padding: 25px;
                background: #f5f7fa;
                color: #333;
            }}

            h1 {{
                color: #2c3e50;
                border-bottom: 3px solid #4CAF50;
                padding-bottom: 8px;
                font-size: 24px;
            }}

            h2 {{
                color: #34495e;
                margin-top: 20px;
                font-size: 18px;
            }}

            ul {{
                margin: 5px 0 10px 20px;
            }}

            hr {{
                margin: 10px 0;
            }}

            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 8px;
                margin-bottom: 15px;
                background: white;
                border-radius: 8px;
                overflow: hidden;
                page-break-inside: avoid;
            }}

            th {{
                background: #4CAF50;
                color: white;
                padding: 8px;
                text-align: left;
            }}

            td {{
                padding: 8px;
                border-bottom: 1px solid #ddd;
            }}
            
            tr:hover {{
                background-color: transparent;
            }}


            img {{
                display: block;
                margin: 10px auto;
                max-width: 100%;
                height: auto;
                page-break-inside: avoid;
            }}


            .section {{
                background: white;
                padding: 15px;
                border-radius: 8px;
                box-shadow: 0 3px 6px rgba(0,0,0,0.08);
                margin-bottom: 15px;
                page-break-inside: avoid;
            }}


            .good {{
                color: #2e7d32;
                font-weight: bold;
            }}

            .bad {{
                color: #c62828;
                font-weight: bold;
            }}

            @page {{
                size: A4;
                margin: 10mm;
            }}
        </style>
    </head>

    <body>
        <div class="section">
            {content}
        </div>
    </body>
    </html>
    """