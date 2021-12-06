def main(input):
    fish_ages = [int(age) for age in input.read().split(",")]
    fish_sums = [sum(int(age) == idx for age in fish_ages) for idx in range(9)]

    total = [sum(fish_sums)]
    for _ in range(256):
        new_fishes = fish_sums[0]
        fish_sums = fish_sums[1:] + [new_fishes]
        fish_sums[6] += new_fishes 
        total.append(sum(fish_sums))

    return total[80], total[256]

# --------------------------------------------------------- # 
import os
from pathlib import Path


curr_dir = Path(__file__).parent

with (curr_dir / "test_input.txt").open() as input:
    assert os.stat(input.fileno()).st_size, "test_input.txt is empty!"
    part1, part2 = main(input)
    part1_expected = 5934
    assert part1 == part1_expected, f"Incorrect for test1. Expected: {part1_expected}. Actual: {part1}"
    part2_expected = 26984457539
    assert part2 == part2_expected, f"Incorrect for test2. Expected: {part2_expected}. Actual: {part2}"

with (curr_dir / "input.txt").open() as input:
    assert os.stat(input.fileno()).st_size, "input.txt is empty!"
    part1, part2 = main(input)
    print(f"PART1: {part1}")
    print(f"PART2: {part2}")
    part1_expected = 355386
    assert part1 == part1_expected, f"Incorrect for part1. Expected: {part1_expected}. Actual: {part1}"
    part2_expected = 1613415325809
    assert part2 == part2_expected, f"Incorrect for part2. Expected: {part2_expected}. Actual: {part2}"

