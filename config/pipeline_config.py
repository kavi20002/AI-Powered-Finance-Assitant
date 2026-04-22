from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"
LOG_DIR = BASE_DIR / "logs"

DATASETS = {
    "normal": DATA_DIR / "scenario1_normal.csv",
    "overspend": DATA_DIR / "scenario2_overspend.csv",
    "edge": DATA_DIR / "scenario3_edge.csv",
}
BUDGET_PATH = DATA_DIR / "budget.json"
REPORT_PATH = OUTPUT_DIR / "monthly_report.md"
TRACE_PATH = LOG_DIR / "agent_trace.json"
DEFAULT_MONTHLY_INCOME = 10000.0
DEFAULT_MODEL = "llama3"
DEFAULT_BASE_CURRENCY = "USD"
DEFAULT_TARGET_CURRENCY = "LKR"
DEFAULT_SAVINGS_RATIO = 0.20