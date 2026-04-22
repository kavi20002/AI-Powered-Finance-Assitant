import sys
from orchestrator.pipeline import run_pipeline
from state.shared_state import create_initial_state
from config.pipeline_config import DEFAULT_MONTHLY_INCOME


def main():

    dataset = "normal"

    if len(sys.argv) > 1:
        dataset = sys.argv[1].lower()

    valid_datasets = ["normal", "overspend", "edge"]

    if dataset not in valid_datasets:
        print(f"⚠️ Invalid dataset '{dataset}'. Falling back to 'normal'.")
        dataset = "normal"

    print("\n==============================")
    print("💰 AI-Powered Finance Assistant")
    print(f"📊 Mode: {dataset.upper()}")
    print("==============================\n")

    try:

        state = create_initial_state(monthly_income=DEFAULT_MONTHLY_INCOME)

        result = run_pipeline(state, dataset=dataset)

        print("\n📌 FINAL RESULT")
        print(result.get("final_summary", "No summary available."))

        print("\n📁 OUTPUT FILES")
        print("Report:", result.get("report_path", "not created"))
        print("Trace :", result.get("trace_path", "not created"))

        print("\n✅ Execution completed successfully!")

    except Exception as e:
        print("\n❌ ERROR OCCURRED")
        print(str(e))

if __name__ == "__main__":
    main()