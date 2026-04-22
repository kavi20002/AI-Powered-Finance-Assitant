from pathlib import Path
import csv
import json

from config.pipeline_config import DATASETS, BUDGET_PATH


def write_csv(path: Path, rows: list[list]):
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "description", "category", "amount"])
        writer.writerows(rows)

def generate_normal():
    rows = [
        ["2026-04-01", "Breakfast", "food", 300],
        ["2026-04-02", "Bus", "transport", 150],
        ["2026-04-03", "Lunch", "food", 450],
        ["2026-04-04", "Movie", "entertainment", 800],
        ["2026-04-05", "Grocery", "food", 1200],
        ["2026-04-06", "Taxi", "transport", 300],
        ["2026-04-07", "Netflix", "entertainment", 600],
    ]
    write_csv(DATASETS["normal"], rows)


def generate_overspend():
    rows = [
        ["2026-04-01", "Restaurant", "food", 1200],
        ["2026-04-02", "Taxi", "transport", 800],
        ["2026-04-03", "Fast food", "food", 900],
        ["2026-04-04", "Concert", "entertainment", 2500],
        ["2026-04-05", "Shopping", "entertainment", 3000],
    ]
    write_csv(DATASETS["overspend"], rows)


def generate_edge():
    rows = [
        ["2026-04-01", "Unknown", "", 500],
        ["2026-04-02", "Invalid", "food", "abc"],
        ["2026-04-03", "Zero", "transport", 0],
        ["2026-04-04", "Negative", "food", -200],
        ["2026-04-05", "Huge", "entertainment", 100000],
    ]
    write_csv(DATASETS["edge"], rows)

def generate_budget():
    BUDGET_PATH.parent.mkdir(parents=True, exist_ok=True)

    data = {
        "food": 3000,
        "transport": 1500,
        "entertainment": 2000,
    }

    with open(BUDGET_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    generate_normal()
    generate_overspend()
    generate_edge()
    generate_budget()

    print("✅ All datasets and budget generated successfully!")