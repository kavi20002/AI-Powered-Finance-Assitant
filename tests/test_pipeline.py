import json
from orchestrator.pipeline import run_pipeline
from state.shared_state import create_initial_state


def test_pipeline_end_to_end(tmp_path):
    csv_path = tmp_path / "transactions.csv"
    budget_path = tmp_path / "budget.json"
    report_path = tmp_path / "monthly_report.md"
    trace_path = tmp_path / "agent_trace.json"

    csv_path.write_text(
        "date,description,category,amount\n"
        "2026-01-01,Lunch,food,500\n"
        "2026-01-02,Bus,transport,200\n"
        "2026-01-03,Movie,entertainment,1000\n",
        encoding="utf-8",
    )
    budget_path.write_text(
        json.dumps(
            {"food": 2000, "transport": 1000, "entertainment": 1500},
            indent=2,
        ),
        encoding="utf-8",
    )
    state = create_initial_state(monthly_income=10000)

    final_state = run_pipeline(
        state,
        csv_path=str(csv_path),
        budget_path=str(budget_path),
        report_path=str(report_path),
        trace_path=str(trace_path),
    )
    assert report_path.exists()
    assert trace_path.exists()
    
    report_content = report_path.read_text(encoding="utf-8")
    assert "Finance" in report_content or "Report" in report_content

    trace_data = json.loads(trace_path.read_text())
    assert isinstance(trace_data, list)
    assert len(trace_data) >= 4

    assert any(entry["status"] == "success" for entry in trace_data)

    assert "successfully" in final_state["final_summary"].lower()