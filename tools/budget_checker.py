from __future__ import annotations

from pathlib import Path
from typing import Any
import json


def _safe_float(value: Any) -> float:
    try:
        return float(str(value).replace(",", "").strip())
    except Exception:
        return 0.0

def read_budget_json(file_path: str) -> dict[str, float]:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Budget file not found: {file_path}")

    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)


    return {
        str(k).strip().lower(): round(_safe_float(v), 2)
        for k, v in data.items()
    }

def compare_budget_vs_spending(
        budget: dict[str, float],
        actuals: dict[str, float],
) -> dict[str, Any]:

    result: dict[str, Any] = {}

    actuals = {str(k).strip().lower(): _safe_float(v) for k, v in actuals.items()}

    all_categories = sorted(set(budget.keys()) | set(actuals.keys()))

    for category in all_categories:
        budget_limit = round(_safe_float(budget.get(category, 0.0)), 2)
        spent = round(_safe_float(actuals.get(category, 0.0)), 2)

        if spent < 0:
            spent = 0

        difference = round(budget_limit - spent, 2)

        if category not in budget:
            status = "unplanned"
            advice = "This category is not in your budget."
        elif spent == 0:
            status = "not_used"
            advice = "No spending recorded in this category."
        elif difference < 0:
            status = "overspent"
            advice = f"Reduce spending by {abs(difference):,.2f} next month."
        else:
            status = "within_budget"
            advice = f"You still have {difference:,.2f} left in this category."

        result[category] = {
            "budget": budget_limit,
            "spent": spent,
            "difference": difference,
            "status": status,
            "advice": advice,
        }

    return result

def build_budget_overview(analysis: dict[str, Any]) -> str:
    overspent = [k for k, v in analysis.items() if v.get("status") == "overspent"]
    unplanned = [k for k, v in analysis.items() if v.get("status") == "unplanned"]

    if not overspent and not unplanned:
        return "Great job. All categories are within budget."

    messages = []

    if overspent:
        messages.append("Overspent: " + ", ".join(sorted(overspent)))

    if unplanned:
        messages.append("Unplanned: " + ", ".join(sorted(unplanned)))

    return " | ".join(messages)