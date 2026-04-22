from __future__ import annotations

from pathlib import Path
from time import perf_counter

from config.llm import invoke_llm
from config.pipeline_config import DEFAULT_MODEL
from state.shared_state import SharedState, add_trace
from tools.budget_checker import (
    build_budget_overview,
    compare_budget_vs_spending,
    read_budget_json,
)


class BudgetAdvisorAgent:
    def __init__(self, budget_path: str, prompt_path: str, model: str = DEFAULT_MODEL):
        self.budget_path = budget_path
        self.prompt_path = prompt_path
        self.model = model

    def _load_prompt(self) -> str:
        return Path(self.prompt_path).read_text(encoding="utf-8").strip()

    def run(self, state: SharedState) -> SharedState:
        start = perf_counter()

        try:
            expense_summary = state.get("expense_summary", {}) or {}

            budget = read_budget_json(self.budget_path)

            budget = {k.lower(): v for k, v in budget.items()}

            analysis = compare_budget_vs_spending(budget, expense_summary)
            overview = build_budget_overview(analysis)

            state["budget"] = budget
            state["budget_analysis"] = analysis
            state["budget_overview"] = overview

            # ✅ Better formatted prompt
            prompt = self._load_prompt()
            llm_input = f"""{prompt}
            === Budget Data ==={budget}
            === Spending Analysis ==={analysis}
            === Summary ==={overview}"""

            llm_output = invoke_llm(llm_input, model=self.model)

            if llm_output:
                state["llm_budget_output"] = llm_output
            else:
                state["llm_budget_output"] = overview

            overspent_count = len(
                [v for v in analysis.values() if v.get("status") == "overspent"]
            )

            add_trace(
                state,
                agent="BudgetAdvisorAgent",
                event="completed",
                details={
                    "categories": len(analysis),
                    "overspent_categories": overspent_count,
                    "duration_ms": round((perf_counter() - start) * 1000, 2),
                },
            )

        except Exception as exc:
            add_trace(
                state,
                agent="BudgetAdvisorAgent",
                event="failed",
                status="error",
                details={"error": str(exc)},
            )

            state["llm_budget_output"] = f"⚠️ Budget analysis failed: {exc}"

        return state