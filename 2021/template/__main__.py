from pathlib import Path


def main(input):
    values = [int(in_line) for in_line in input]
    result1 = ...
    result2 = ...
    return result1, result2


# --------------------------------------------------------- # 

curr_dir = Path(__file__).parent

with (curr_dir / "test_input.txt").open() as input:
    part1, part2 = main(input)
    assert part1 == ...
    assert part2 == ...

with (curr_dir / "input.txt").open() as input:
    part1, part2 = main(input)
    # assert part1 == ...
    # assert part2 == ...
    print(f"PART1: {part1}")
    print(f"PART2: {part2}")

