from langgraph.graph import StateGraph, END
from state.shared_state import SharedState

from agents.expense_tracker_agent import ExpenseTrackerAgent
from agents.budget_advisor_agent import BudgetAdvisorAgent
from agents.savings_goal_agent import SavingsGoalAgent
from agents.report_logger_agent import ReportLoggerAgent

exp = ExpenseTrackerAgent()
bud = BudgetAdvisorAgent()
sav = SavingsGoalAgent()
rep = ReportLoggerAgent()

def run_pipeline(state):

    builder = StateGraph(SharedState)

    builder.add_node("expense", exp.run)
    builder.add_node("budget", bud.run)
    builder.add_node("savings", sav.run)
    builder.add_node("report", rep.run)

    builder.set_entry_point("expense")

    builder.add_edge("expense", "budget")
    builder.add_edge("budget", "savings")
    builder.add_edge("savings", "report")
    builder.add_edge("report", END)

    graph = builder.compile()
    return graph.invoke(state)