from tools.report_writer import write_report, write_log

class ReportLoggerAgent:
    def run(self, state):
        report = f"""
# Monthly Report

Expenses:
{state['expense_summary']}

Budget:
{state['budget_analysis']}

Savings:
{state['savings_context']}
"""

        write_report("outputs/monthly_report.md", report)
        write_log("logs/agent_trace.json", state["trace"])

        state["final_summary"] = "Done"
        return state