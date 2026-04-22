from tools.budget_checker import compare_budget_vs_spending

def test_budget():
    budget = {"food": 100}
    actual = {"food": 150}

    result = compare_budget_vs_spending(budget, actual)

    assert result["food"]["status"] == "overspent"