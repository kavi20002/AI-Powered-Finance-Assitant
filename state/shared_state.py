from __future__ import annotations
from datetime import datetime, timezone
from typing import TypedDict, Any
import uuid


class SharedState(TypedDict, total=False):
    # =========================
    # META
    # =========================
    run_id: str
    generated_at: str
    monthly_income: float

    # =========================
    # EXPENSE
    # =========================
    transactions: list[dict[str, Any]]
    expense_summary: dict[str, float]
    expense_total: float

    # =========================
    # BUDGET
    # =========================
    budget: dict[str, float]
    budget_analysis: dict[str, Any]
    budget_overview: str

    # =========================
    # SAVINGS
    # =========================
    savings_context: dict[str, Any]
    leftover_balance: float

    # =========================
    # ML + VISUALS ✅ NEW
    # =========================
    forecast: float              # 📈 predicted spending
    bar_chart: str              # 📊 bar chart path
    pie_chart: str              # 🥧 pie chart path

    # =========================
    # OUTPUT FILES
    # =========================
    report_path: str
    report_image: str           # 🖼 PNG
    report_pdf: str             # 📄 PDF
    trace_path: str

    # =========================
    # FINAL OUTPUT
    # =========================
    final_summary: str
    trace: list[dict[str, Any]]


def create_initial_state(
        run_id: str | None = None,
        monthly_income: float = 10000.0,
) -> SharedState:
    return {
        "run_id": run_id or str(uuid.uuid4())[:8],
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "monthly_income": monthly_income,

        "transactions": [],
        "expense_summary": {},
        "expense_total": 0.0,

        "budget": {},
        "budget_analysis": {},
        "budget_overview": "",

        "savings_context": {},
        "leftover_balance": 0.0,

        # ✅ NEW FIELDS
        "forecast": 0.0,
        "bar_chart": "",
        "pie_chart": "",

        "report_path": "",
        "report_image": "",
        "report_pdf": "",
        "trace_path": "",

        "final_summary": "",
        "trace": [],
    }


def add_trace(
        state: SharedState,
        agent: str,
        event: str,
        status: str = "success",
        details: dict[str, Any] | None = None,
) -> SharedState:
    state.setdefault("trace", []).append({
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "agent": agent,
        "event": event,
        "status": status,
        "details": details or {},
    })
    return state