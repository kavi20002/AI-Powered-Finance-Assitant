from typing import TypedDict, Dict, Any, List

class SharedState(TypedDict, total=False):
    transactions: List[Dict]
    expense_summary: Dict[str, float]
    budget: Dict[str, float]
    budget_analysis: Dict
    savings_context: Dict
    final_summary: str
    report_path: str
    trace: List[Dict]

def create_initial_state() -> SharedState:
    return {
        "transactions": [],
        "expense_summary": {},
        "budget": {},
        "budget_analysis": {},
        "savings_context": {},
        "final_summary": "",
        "report_path": "",
        "trace": []
    }