def get_styled_html(content: str) -> str:
    return f"""
    <html>
    <head>
        <style>
            body {{
                font-family: 'Segoe UI', sans-serif;
                padding: 40px;
                background: #f5f7fa;
                color: #333;
            }}

            h1 {{
                color: #2c3e50;
                border-bottom: 3px solid #4CAF50;
                padding-bottom: 10px;
            }}

            h2 {{
                color: #34495e;
                margin-top: 30px;
            }}

            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 10px;
                margin-bottom: 20px;
                background: white;
                border-radius: 8px;
                overflow: hidden;
            }}

            th {{
                background: #4CAF50;
                color: white;
                padding: 10px;
                text-align: left;
            }}

            td {{
                padding: 10px;
                border-bottom: 1px solid #ddd;
            }}

            tr:hover {{
                background-color: #f1f1f1;
            }}

            .card {{
                background: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                margin-bottom: 20px;
            }}

            .good {{
                color: green;
                font-weight: bold;
            }}

            .bad {{
                color: red;
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        {content}
    </body>
    </html>
    """