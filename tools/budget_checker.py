import json

def read_budget_json(path):
    with open(path) as f:
        return json.load(f)

def compare_budget_vs_spending(budget, actual):
    result = {}
    for cat, limit in budget.items():
        spent = actual.get(cat, 0)
        result[cat] = {
            "spent": spent,
            "budget": limit,
            "status": "overspent" if spent > limit else "ok"
        }
    return result