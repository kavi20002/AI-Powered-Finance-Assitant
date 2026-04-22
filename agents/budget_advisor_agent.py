from tools.budget_checker import read_budget_json, compare_budget_vs_spending

class BudgetAdvisorAgent:
    def run(self, state):
        budget = read_budget_json("data/budget.json")
        analysis = compare_budget_vs_spending(budget, state["expense_summary"])

        state["budget"] = budget
        state["budget_analysis"] = analysis
        return state