from __future__ import annotations
from typing import Any
from datetime import datetime, timezone
import requests

def fetch_currency_context(
        base_currency: str = "USD",
        target_currency: str = "LKR",
) -> dict[str, Any]:

    url = (
        "https://api.frankfurter.app/latest"
        f"?from={base_currency.upper()}&to={target_currency.upper()}"
    )

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        rate = data.get("rates", {}).get(target_currency.upper(), None)

        return {
            "base": data.get("base", base_currency.upper()),
            "date": data.get("date", ""),
            "rates": data.get("rates", {}),
            "exchange_rate": rate,
            "fetched_at": datetime.now(timezone.utc).isoformat(),
        }

    except Exception as exc:
        return {
            "error": f"API request failed: {exc}",
            "base": base_currency.upper(),
            "date": "",
            "rates": {},
            "exchange_rate": None,
            "fetched_at": datetime.now(timezone.utc).isoformat(),
        }

def suggest_savings_target(
        leftover_income: float,
        ratio: float = 0.20,
        floor: float = 0.0,
) -> dict[str, Any]:

    if ratio < 0 or ratio > 1:
        ratio = 0.20

    leftover_income = round(leftover_income, 2)

    if leftover_income <= 0:
        return {
            "leftover_income": leftover_income,
            "goal_ratio": ratio,
            "target": 0,
            "message": "⚠️ No savings possible due to overspending.",
        }

    target = max(round(leftover_income * ratio, 2), floor)

    return {
        "leftover_income": leftover_income,
        "goal_ratio": ratio,
        "target": target,
        "message": f"Save about {target:,.2f} each month for a steady goal.",
    }

def build_savings_context(
        leftover_income: float,
        base_currency: str = "USD",
        target_currency: str = "LKR",
        ratio: float = 0.20,
) -> dict[str, Any]:

    api_data = fetch_currency_context(base_currency, target_currency)
    plan = suggest_savings_target(leftover_income, ratio=ratio)

    insight = None
    if api_data.get("exchange_rate"):
        insight = f"1 {api_data['base']} ≈ {api_data['exchange_rate']} {target_currency}"

    return {
        "api": api_data,
        "plan": plan,
        "insight": insight,
    }