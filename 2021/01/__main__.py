from pathlib import Path


curr_dir = Path(__file__).parent
with (curr_dir / "input.txt").open() as input:
    values = [int(in_line) for in_line in input]

    def window_sum_increases(window):
        window_sums = [sum(values[i:i + window]) for i in range(len(values) + 1 - window)]
        return sum(b < a for a, b in zip(window_sums[1:], window_sums[:-1]))

    print(f"PART1: {window_sum_increases(1)}")
    print(f"PART2: {window_sum_increases(3)}")

