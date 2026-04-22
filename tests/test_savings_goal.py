from tools.savings_api import suggest_savings_target

def test_savings_target():
    result = suggest_savings_target(1000)

    assert result["target"] == 200.0
    assert result["goal_ratio"] == 0.20

def test_zero_income():
    result = suggest_savings_target(0)

    assert result["target"] == 0
    assert result["leftover_income"] == 0


def test_negative_income():
    result = suggest_savings_target(-500)

    assert result["target"] == 0


def test_custom_ratio():
    result = suggest_savings_target(1000, ratio=0.5)

    assert result["target"] == 500


def test_rounding():
    result = suggest_savings_target(1234.56)

    assert round(result["target"], 2) == 246.91