from tools.savings_api import fetch_currency, suggest_savings

class SavingsGoalAgent:
    def run(self, state):
        total = sum(state["expense_summary"].values())
        income = 10000  # demo value
        leftover = income - total

        api = fetch_currency()
        savings = suggest_savings(leftover)

        state["savings_context"] = {
            "api": api,
            "plan": savings
        }
        return state