from tools.savings_api import suggest_savings

def test_savings():
    result = suggest_savings(1000)
    assert result["target"] == 200