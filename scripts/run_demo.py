from state.shared_state import create_initial_state
from orchestrator.pipeline import run_pipeline

def run():
    state = create_initial_state()
    result = run_pipeline(state)

    print("=== DEMO RUN ===")
    print(result["final_summary"])

if __name__ == "__main__":
    run()