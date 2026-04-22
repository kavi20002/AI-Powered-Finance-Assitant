# 💰 AI-Powered Finance Assistant

An intelligent **multi-agent system** that analyzes personal financial data, evaluates budgets, suggests savings, and generates **professional reports (Markdown, Image, PDF)**.

---

## 🚀 Features

- 📊 Expense tracking from CSV datasets
- 💸 Budget analysis with overspending detection
- 💡 Smart savings recommendations
- 🤖 AI integration (LangChain + Ollama)
- 🧾 Report generation:
    - Markdown (.md)
    - HTML (styled)
    - Image (.png)
    - PDF (.pdf)
- 🧠 Multi-agent pipeline (LangGraph)
- 📝 Execution trace logging
- ✅ Unit tested (pytest)

---

## 🧠 System Architecture


ExpenseTrackerAgent
↓
BudgetAdvisorAgent
↓
SavingsGoalAgent
↓
ReportLoggerAgent


Each agent processes data and passes results through a shared state.

---

## 📁 Project Structure


AI-Powered-Finance-Assistant/
│
├── agents/
├── config/
├── data/
├── docs/
├── logs/
├── orchestrator/
├── outputs/
├── prompts/
├── scripts/
├── state/
├── tests/
├── tools/
│
├── main.py
├── requirements.txt
└── README.md


---

## ⚙️ Installation

### 1. Clone repository

```bash
git clone https://github.com/your-username/AI-Powered-Finance-Assistant.git
cd AI-Powered-Finance-Assistant
2. Create virtual environment
python -m venv venv
venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Install wkhtmltopdf (for PDF)

Download:
https://wkhtmltopdf.org/downloads.html

Update path in:

tools/report_to_pdf.py

Example:

config = pdfkit.configuration(
    wkhtmltopdf=r"C:\Users\your-username\wkhtmltopdf\bin\wkhtmltopdf.exe"
)
▶️ How to Run
Run default
python main.py
Run different datasets
python main.py normal
python main.py overspend
python main.py edge
📊 Output Files

After running:

outputs/monthly_report.md
outputs/monthly_report.html
docs/monthly_report.png
docs/monthly_report.pdf
logs/agent_trace.json
📦 Dataset Files

Located in data/:

scenario1_normal.csv
scenario2_overspend.csv
scenario3_edge.csv
budget.json
🧾 Report Flow
Markdown → HTML → Styled UI → PNG → PDF
🧪 Run Tests
python -m pytest
🤖 AI Integration
LangChain
LangGraph
Ollama (llama3)

If LLM is not available → system still works normally.

⚠️ Notes
Emojis replaced with icons for PDF compatibility
wkhtmltopdf required for PDF generation
Zoom used to fit content into single page
🔥 Future Improvements
Charts (bar / pie)
Dashboard UI
Web application
API deployment
Financial forecasting
👨‍💻 Author

Kavidu Keshan

📜 License

Educational use only