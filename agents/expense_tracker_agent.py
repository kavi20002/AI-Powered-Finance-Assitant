from __future__ import annotations

from pathlib import Path
from time import perf_counter

from config.llm import invoke_llm
from config.pipeline_config import DEFAULT_MODEL
from state.shared_state import SharedState, add_trace
from tools.csv_reader import (
    calculate_total_spending,
    get_top_category,
    read_transactions_csv,
    summarize_by_category,
)


class ExpenseTrackerAgent:
    def __init__(self, csv_path: str, prompt_path: str, model: str = DEFAULT_MODEL):
        self.csv_path = csv_path
        self.prompt_path = prompt_path
        self.model = model

    def _load_prompt(self) -> str:
        return Path(self.prompt_path).read_text(encoding="utf-8").strip()

    def run(self, state: SharedState) -> SharedState:
        start = perf_counter()

        try:
            transactions = read_transactions_csv(self.csv_path) or []

            if not transactions:
                state["expense_summary"] = {}
                state["expense_total"] = 0
                state["llm_expense_output"] = "⚠️ No transactions found."
                return state

            summary = summarize_by_category(transactions)

            summary = {k.lower(): v for k, v in summary.items()}

            total_spent = calculate_total_spending(transactions)
            top_category, top_value = get_top_category(summary)

            state["transactions"] = transactions
            state["expense_summary"] = summary
            state["expense_total"] = total_spent

            prompt = self._load_prompt()

            llm_input = f"""{prompt}
            === Expense Summary ==={summary}
            === Total Spending ==={total_spent}
            === Top Category ==={top_category} ({top_value})"""

            llm_output = invoke_llm(llm_input, model=self.model)

            if llm_output:
                state["llm_expense_output"] = llm_output
            else:
                state["llm_expense_output"] = (
                    f"Top spending category is '{top_category}' with total {top_value}."
                )

            add_trace(
                state,
                agent="ExpenseTrackerAgent",
                event="completed",
                details={
                    "transactions": len(transactions),
                    "total_spent": total_spent,
                    "top_category": top_category,
                    "duration_ms": round((perf_counter() - start) * 1000, 2),
                },
            )

        except Exception as exc:
            add_trace(
                state,
                agent="ExpenseTrackerAgent",
                event="failed",
                status="error",
                details={"error": str(exc)},
            )

            state["expense_summary"] = {}
            state["expense_total"] = 0
            state["llm_expense_output"] = f"⚠️ Expense tracking failed: {exc}"

        return state