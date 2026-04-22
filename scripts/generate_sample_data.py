import json
import csv

def generate_csv():
    with open("data/transactions.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "description", "category", "amount"])
        writer.writerow(["2026-01-01", "Lunch", "food", 500])
        writer.writerow(["2026-01-02", "Bus", "transport", 200])
        writer.writerow(["2026-01-03", "Movie", "entertainment", 1000])

def generate_budget():
    data = {
        "food": 2000,
        "transport": 1000,
        "entertainment": 1500
    }
    with open("data/budget.json", "w") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    generate_csv()
    generate_budget()
    print("Sample data generated.")