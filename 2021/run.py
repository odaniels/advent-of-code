from datetime import date
from utils import run
from pathlib import Path
from rich.console import Console
from rich.table import Table
import sys


if __name__ == "__main__":
    try:
        arg = sys.argv[1]
    except IndexError:
        arg = str(date.today())[-2:]

    if arg == "stats":
        console = Console()
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Date", style="dim", width=12)
        table.add_column("Test 1")
        table.add_column("Test 2")
        table.add_column("Test Execution Time \[us]", justify="right")
        table.add_column("Part 1")
        table.add_column("Part 2")
        table.add_column("Execution Time \[us]", justify="right")

        for i in (f"{1 + j:02d}" for j in range(25)):
            console.print(f"Running day {i}...")
            try:
                exec(f"from day{i} import main")
                test = run(main.main, Path(main.__file__).parent /  "test_input.txt", *main.TEST_EXPECTED, False)
                puzzle = run(main.main, Path(main.__file__).parent /  "input.txt", *main.PUZZLE_EXPECTED, False)
            except:
                test = None, None, None
                puzzle = None, None, None

            table.add_row(
                f"{i}",
                "[green]PASS[/green]" if test[0] else "[red]FAIL[/red]" if test[0] is not None else "-",
                "[green]PASS[/green]" if test[1] else "[red]FAIL[/red]" if test[1] is not None else "-",
                str(test[2].seconds * 1000000 + test[2].microseconds) if test[2] is not None else "-",
                "[green]PASS[/green]" if puzzle[0] else "[red]FAIL[/red]" if puzzle[0] is not None else "-",
                "[green]PASS[/green]" if puzzle[1] else "[red]FAIL[/red]" if puzzle[1] is not None else "-",
                str(puzzle[2].seconds * 1000000 + puzzle[2].microseconds) if puzzle[2] is not None else "-"
            )

        console.clear()
        console.print(table)
    else:
        exec(f"from day{arg} import main")
        run(main.main, Path(main.__file__).parent /  "test_input.txt", *main.TEST_EXPECTED)
        run(main.main, Path(main.__file__).parent /  "input.txt", *main.PUZZLE_EXPECTED)