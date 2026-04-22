from tools.budget_checker import compare_budget_vs_spending

def test_budget_status_overspent():
    budget = {"food": 100}
    actual = {"food": 150}

    result = compare_budget_vs_spending(budget, actual)

    assert result["food"]["status"] == "overspent"
    assert result["food"]["difference"] == -50


def test_budget_status_within_budget():
    budget = {"food": 200}
    actual = {"food": 150}

    result = compare_budget_vs_spending(budget, actual)

    assert result["food"]["status"] == "within_budget"
    assert result["food"]["difference"] == 50

def test_budget_not_used():
    budget = {"food": 100}
    actual = {"food": 0}

    result = compare_budget_vs_spending(budget, actual)

    assert result["food"]["status"] == "not_used"


def test_budget_missing_category():
    budget = {"food": 100}
    actual = {"transport": 50}

    result = compare_budget_vs_spending(budget, actual)

    assert "transport" in result
    assert result["transport"]["spent"] == 50


def test_empty_inputs():
    result = compare_budget_vs_spending({}, {})

    assert result == {}