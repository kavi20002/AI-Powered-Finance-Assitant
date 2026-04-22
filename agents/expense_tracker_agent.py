from tools.csv_reader import read_transactions_csv, summarize_by_category

class ExpenseTrackerAgent:
    def run(self, state):
        tx = read_transactions_csv("data/transactions.csv")
        summary = summarize_by_category(tx)

        state["transactions"] = tx
        state["expense_summary"] = summary
        return state