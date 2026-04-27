from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()


def header(title, dataset):
    console.print(
        Panel.fit(
            f"[bold green]{title}[/bold green]\n[cyan]Mode: {dataset.upper()}[/cyan]",
            title="🚀 Finance AI System",
            border_style="green"
        )
    )


def section(title):
    console.print(f"\n[bold yellow]▶ {title}[/bold yellow]")


def success(msg):
    console.print(f"[green]✔ {msg}[/green]")


def info(msg):
    console.print(f"[cyan]➤ {msg}[/cyan]")


def warn(msg):
    console.print(f"[red]⚠ {msg}[/red]")


def final_block(result):
    summary = result.get("final_summary", "No summary available.")

    console.print(
        Panel(
            f"[white]{summary}[/white]",
            title="📌 FINAL RESULT",
            border_style="blue"
        )
    )

    console.print(
        Panel(
            f"[green]Report:[/green] {result.get('report_path')}\n"
            f"[green]Trace :[/green] {result.get('trace_path')}",
            title="📁 OUTPUT FILES",
            border_style="magenta"
        )
    )

    console.print("[bold green]✔ Execution completed successfully![/bold green]")