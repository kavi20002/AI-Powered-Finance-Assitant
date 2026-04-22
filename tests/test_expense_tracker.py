from tools.csv_reader import summarize_by_category

def test_summary():
    data = [
        {"category": "food", "amount": 100},
        {"category": "food", "amount": 50},
    ]
    result = summarize_by_category(data)
    assert result["food"] == 150