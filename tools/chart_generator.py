import matplotlib.pyplot as plt
from pathlib import Path


def generate_bar_chart(summary: dict, output_path: str):
    categories = list(summary.keys())
    values = list(summary.values())

    # ✅ Color logic: red for negative, blue for positive
    colors = ["red" if v < 0 else "blue" for v in values]

    plt.figure()
    plt.bar(categories, values, color=colors)

    plt.title("Expense by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")

    # ✅ Add zero reference line
    plt.axhline(0)

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path)
    plt.close()

    return output_path


def generate_pie_chart(summary: dict, output_path: str):
    categories = []
    values = []

    for k, v in summary.items():
        if v > 0:
            categories.append(k)
            values.append(v)

    if not values:
        categories = ["No Data"]
        values = [1]

    plt.figure()
    plt.pie(values, labels=categories, autopct='%1.1f%%')
    plt.title("Expense Distribution")

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path)
    plt.close()

    return output_path