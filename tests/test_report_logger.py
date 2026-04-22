import json
from tools.report_writer import build_report_markdown, write_report, write_trace_log

def test_build_report_markdown():
    state = {
        "run_id": "demo123",
        "monthly_income": 10000,
        "expense_summary": {"food": 500, "transport": 200},
        "budget_analysis": {
            "food": {"budget": 1000, "spent": 500, "difference": 500, "status": "within_budget"},
            "transport": {"budget": 1000, "spent": 200, "difference": 800, "status": "within_budget"},
        },
        "savings_context": {
            "api": {"base": "USD", "date": "2026-04-21", "rates": {"LKR": 300}},
            "plan": {
                "target": 1840,
                "goal_ratio": 0.20,
                "message": "Save about 1,840.00 each month for a steady goal.",
            },
        },
        "trace": [{"agent": "A"}],
    }

    report = build_report_markdown(state)

    assert "# 💰 AI Finance Monthly Report" in report
    assert "Expense Breakdown" in report
    assert "Savings Plan" in report

    assert "food" in report.lower()
    assert "transport" in report.lower()
    assert "1840" in report or "1,840" in report

def test_write_report_and_trace(tmp_path):
    report_path = tmp_path / "report.md"
    trace_path = tmp_path / "trace.json"

    write_report(str(report_path), "# hello")
    write_trace_log(str(trace_path), [{"agent": "A"}])

    assert report_path.exists()
    assert trace_path.exists()

    assert report_path.read_text() == "# hello"

    trace_data = json.loads(trace_path.read_text())
    assert isinstance(trace_data, list)
    assert trace_data[0]["agent"] == "A"