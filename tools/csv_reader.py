from __future__ import annotations

from pathlib import Path
from typing import Any
import csv


def _safe_float(value: Any) -> float:
    try:
        return float(str(value).replace(",", "").strip())
    except Exception:
        return 0.0

def normalize_category(category: Any) -> str:
    text = str(category or "").strip().lower()

    if not text:
        return "uncategorized"

    aliases = {
        "groceries": "food",
        "dining": "food",
        "meal": "food",
        "bus": "transport",
        "taxi": "transport",
        "ride": "transport",
        "movies": "entertainment",
        "cinema": "entertainment",
    }

    return aliases.get(text, text)

def read_transactions_csv(file_path: str) -> list[dict[str, Any]]:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"CSV file not found: {file_path}")

    transactions: list[dict[str, Any]] = []

    with path.open(mode="r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            amount = round(_safe_float(row.get("amount", 0.0)), 2)

            if amount == 0 and not row.get("description"):
                continue

            transactions.append(
                {
                    "date": str(row.get("date", "")).strip(),
                    "description": str(row.get("description", "")).strip(),
                    "category": normalize_category(row.get("category")),
                    "amount": amount,
                }
            )

    return transactions

def summarize_by_category(transactions: list[dict[str, Any]]) -> dict[str, float]:
    summary: dict[str, float] = {}

    for tx in transactions:
        category = normalize_category(tx.get("category"))
        amount = _safe_float(tx.get("amount", 0.0))  # ⚠️ DO NOT use abs()

        summary[category] = round(summary.get(category, 0.0) + amount, 2)

    return dict(sorted(summary.items()))

def calculate_total_spending(transactions: list[dict[str, Any]]) -> float:
    total = 0.0

    for tx in transactions:
        amount = _safe_float(tx.get("amount", 0.0))

        if amount < 0:
            continue

        total += amount

    return round(total, 2)

def get_top_category(summary: dict[str, float]) -> tuple[str, float]:
    if not summary:
        return ("none", 0.0)

    if all(v == 0 for v in summary.values()):
        return ("none", 0.0)

    category = max(summary, key=summary.get)
    return category, round(summary[category], 2)