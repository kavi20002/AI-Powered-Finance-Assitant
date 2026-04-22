from tools.csv_reader import summarize_by_category, calculate_total_spending


def test_summarize_by_category():
    transactions = [
        {"category": "food", "amount": 100},
        {"category": "food", "amount": 50},
        {"category": "transport", "amount": 25},
    ]

    result = summarize_by_category(transactions)

    assert result["food"] == 150
    assert result["transport"] == 25


def test_calculate_total_spending():
    transactions = [
        {"category": "food", "amount": 100},
        {"category": "transport", "amount": 25},
    ]

    assert calculate_total_spending(transactions) == 125

def test_empty_transactions():
    assert summarize_by_category([]) == {}
    assert calculate_total_spending([]) == 0

def test_invalid_amounts():
    transactions = [
        {"category": "food", "amount": "abc"},  # invalid
        {"category": "food", "amount": None},   # invalid
    ]

    result = summarize_by_category(transactions)

    assert result["food"] == 0


def test_missing_category():
    transactions = [
        {"category": "", "amount": 100},
    ]

    result = summarize_by_category(transactions)

    assert "uncategorized" in result


def test_negative_values():
    transactions = [
        {"category": "food", "amount": -100},
        {"category": "food", "amount": 50},
    ]

    result = summarize_by_category(transactions)

    assert result["food"] == -50