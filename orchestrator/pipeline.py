from __future__ import annotations
from langgraph.graph import END, StateGraph
from agents.budget_advisor_agent import BudgetAdvisorAgent
from agents.expense_tracker_agent import ExpenseTrackerAgent
from agents.report_logger_agent import ReportLoggerAgent
from agents.savings_goal_agent import SavingsGoalAgent
from config.pipeline_config import (
    BUDGET_PATH,
    DATASETS,
    DEFAULT_MODEL,
    REPORT_PATH,
    TRACE_PATH,
)
from state.shared_state import SharedState


def build_pipeline(
        dataset="normal",
        csv_path=None,   # ✅ NEW
        budget_path: str = BUDGET_PATH,
        report_path: str = REPORT_PATH,
        trace_path: str = TRACE_PATH,
        model: str = DEFAULT_MODEL,
):
    if csv_path:
        csv_path = str(csv_path)
    else:
        csv_path = str(DATASETS.get(dataset, DATASETS["normal"]))

    expense_agent = ExpenseTrackerAgent(
        csv_path=csv_path,
        prompt_path="prompts/expense_tracker_prompt.txt",
        model=model,
    )

    budget_agent = BudgetAdvisorAgent(
        budget_path=budget_path,
        prompt_path="prompts/budget_advisor_prompt.txt",
        model=model,
    )

    savings_agent = SavingsGoalAgent(
        prompt_path="prompts/savings_goal_prompt.txt",
        model=model,
    )

    report_agent = ReportLoggerAgent(
        report_path=report_path,
        trace_path=trace_path,
        prompt_path="prompts/report_logger_prompt.txt",
        model=model,
    )

    graph = StateGraph(SharedState)

    graph.add_node("expense", expense_agent.run)
    graph.add_node("budget", budget_agent.run)
    graph.add_node("savings", savings_agent.run)
    graph.add_node("report", report_agent.run)

    graph.set_entry_point("expense")
    graph.add_edge("expense", "budget")
    graph.add_edge("budget", "savings")
    graph.add_edge("savings", "report")
    graph.add_edge("report", END)

    return graph.compile()


def run_pipeline(
        state,
        dataset="normal",
        csv_path=None,
        budget_path=None,
        report_path=None,
        trace_path=None,
):
    pipeline = build_pipeline(
        dataset=dataset,
        csv_path=csv_path,
        budget_path=budget_path or BUDGET_PATH,
        report_path=report_path or REPORT_PATH,
        trace_path=trace_path or TRACE_PATH,
    )

    return pipeline.invoke(state)