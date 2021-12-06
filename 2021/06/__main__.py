from collections import defaultdict


def main(input):
    input_fishes = [int(age) for age in input.read().split(",")]
    fishes_per_age = defaultdict(int)

    for age in input_fishes:
        fishes_per_age[age] += 1

    part1_days, part2_days = 80, 256

    for day in range(part2_days):
        if day == part1_days:
            result1 = sum(age for age in fishes_per_age.values())
        
        next_day = defaultdict(int)
        for age, fishes in fishes_per_age.items():
            if age == 0:
                next_day[8] += fishes
                next_day[6] += fishes
            else:
                next_day[age - 1] += fishes
        fishes_per_age = next_day
    
    result2 = sum(age for age in fishes_per_age.values())
    
    return result1, result2


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

