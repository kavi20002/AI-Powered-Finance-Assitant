import sys
from orchestrator.pipeline import run_pipeline
from state.shared_state import create_initial_state
from config.pipeline_config import DEFAULT_MONTHLY_INCOME
from utils.console_ui import header, final_block, warn

def main():

    dataset = "normal"

    if len(sys.argv) > 1:
        dataset = sys.argv[1].lower()

    valid_datasets = ["normal", "overspend", "edge"]

    if dataset not in valid_datasets:
        print(f"⚠️ Invalid dataset '{dataset}'. Falling back to 'normal'.")
        dataset = "normal"

    header("AI-Powered Finance Assistant", dataset)

    try:
        state = create_initial_state(monthly_income=DEFAULT_MONTHLY_INCOME)

        result = run_pipeline(state, dataset=dataset)

        final_block(result)

    except Exception as e:
        print("\n❌ ERROR OCCURRED")
        warn(str(e))

if __name__ == "__main__":
    main()