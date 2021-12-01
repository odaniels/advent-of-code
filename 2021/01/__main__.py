from pathlib import Path


curr_dir = Path(__file__).parent
with (curr_dir / "input.txt").open() as input:
    values = [int(in_line.split("\n")[0]) for in_line in input]

    def sliding_sum(window_size):
        prev = None
        count = 0
        for i, _ in enumerate(values):
            if i <= len(values) - window_size:
                curr = sum(values[i:i + window_size])
            else:
                break
            if prev:
                count = count + 1 if prev < curr else count
            prev = curr
        return count

    print(f"PART1: {sliding_sum(1)}")
    print(f"PART2: {sliding_sum(3)}")

