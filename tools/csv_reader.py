import csv

def read_transactions_csv(path):
    data = []
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["amount"] = float(row["amount"])
            data.append(row)
    return data

def summarize_by_category(transactions):
    summary = {}
    for t in transactions:
        cat = t["category"]
        summary[cat] = summary.get(cat, 0) + t["amount"]
    return summary