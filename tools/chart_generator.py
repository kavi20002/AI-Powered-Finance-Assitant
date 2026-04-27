import matplotlib.pyplot as plt
from pathlib import Path


def generate_bar_chart(summary: dict, output_path: str):
    categories = list(summary.keys())
    values = list(summary.values())

    plt.figure()
    plt.bar(categories, values)
    plt.title("Expense by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path)
    plt.close()

    return output_path


def generate_pie_chart(summary: dict, output_path: str):
    categories = list(summary.keys())
    values = list(summary.values())

    plt.figure()
    plt.pie(values, labels=categories, autopct='%1.1f%%')
    plt.title("Expense Distribution")

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path)
    plt.close()

    return output_path