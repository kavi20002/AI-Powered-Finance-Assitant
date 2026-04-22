from __future__ import annotations

from pathlib import Path
from time import perf_counter

from config.llm import invoke_llm
from config.pipeline_config import (
    DEFAULT_BASE_CURRENCY,
    DEFAULT_MODEL,
    DEFAULT_SAVINGS_RATIO,
    DEFAULT_TARGET_CURRENCY,
)
from state.shared_state import SharedState, add_trace
from tools.csv_reader import calculate_total_spending
from tools.savings_api import build_savings_context


class SavingsGoalAgent:
    def __init__(
            self,
            prompt_path: str,
            model: str = DEFAULT_MODEL,
            base_currency: str = DEFAULT_BASE_CURRENCY,
            target_currency: str = DEFAULT_TARGET_CURRENCY,
            savings_ratio: float = DEFAULT_SAVINGS_RATIO,
    ):
        self.prompt_path = prompt_path
        self.model = model
        self.base_currency = base_currency
        self.target_currency = target_currency
        self.savings_ratio = savings_ratio

    def _load_prompt(self) -> str:
        return Path(self.prompt_path).read_text(encoding="utf-8").strip()

    def run(self, state: SharedState) -> SharedState:
        start = perf_counter()

        try:
            transactions = state.get("transactions", []) or []
            monthly_income = float(state.get("monthly_income", 0.0))

            total_spent = calculate_total_spending(transactions)
            leftover = round(monthly_income - total_spent, 2)

            savings_context = build_savings_context(
                leftover_income=leftover,
                base_currency=self.base_currency,
                target_currency=self.target_currency,
                ratio=self.savings_ratio,
            )

            state["savings_context"] = savings_context
            state["leftover_balance"] = leftover

            # ✅ Better prompt format
            prompt = self._load_prompt()
            llm_input = f"""{prompt}
            === Financial Summary ===
            Monthly Income: {monthly_income}
            Total Spending: {total_spent}
            Remaining Balance: {leftover}
            === Savings Context ==={savings_context}"""

            llm_output = invoke_llm(llm_input, model=self.model)

            if llm_output:
                state["llm_savings_output"] = llm_output
            else:
                if leftover <= 0:
                    state["llm_savings_output"] = (
                        "⚠️ You have no savings due to overspending. Reduce expenses first."
                    )
                else:
                    target = savings_context.get("plan", {}).get("target", 0)
                    state["llm_savings_output"] = (
                        f"Recommended monthly savings target: {target}."
                    )

            add_trace(
                state,
                agent="SavingsGoalAgent",
                event="completed",
                details={
                    "monthly_income": monthly_income,
                    "total_spent": total_spent,
                    "leftover": leftover,
                    "savings_target": savings_context.get("plan", {}).get("target", 0),
                    "duration_ms": round((perf_counter() - start) * 1000, 2),
                },
            )

        except Exception as exc:
            add_trace(
                state,
                agent="SavingsGoalAgent",
                event="failed",
                status="error",
                details={"error": str(exc)},
            )

            state["savings_context"] = {}
            state["leftover_balance"] = 0
            state["llm_savings_output"] = f"⚠️ Savings calculation failed: {exc}"

        return state