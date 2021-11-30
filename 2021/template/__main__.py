from pathlib import Path


curr_dir = Path(__file__).parent
with (curr_dir / "input.txt").open() as input:
    values = [int(in_line.split("\n")[0]) for in_line in input]
    result = ...
    # print(f"PART1: {result}")
    # print(f"PART2: {result}")

