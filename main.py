from state.shared_state import create_initial_state
from orchestrator.pipeline import run_pipeline

state = create_initial_state()
result = run_pipeline(state)

print("FINAL:", result["final_summary"])