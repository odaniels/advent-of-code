def main(input):
    values = [[b.strip().split() for b in a.split("|")] for a in input.readlines()]
    len_values = [[[len(c) for c in b] for b in a] for a in values]
    output_values = [a[1] for a in len_values]
    result1 = sum(sum(b in [2, 3, 4, 7] for b in a) for a in output_values)

    digits = []
    for value in values:
        all_numbers = value[0] + value[1]
        unique = set(all_numbers)
        decoded = {}

        for number in unique:
            if len(number) == 2:
                decoded[1] = set(number)
            if len(number) == 3:
                decoded[7] = set(number)
            if len(number) == 4:
                decoded[4] = set(number)
            if len(number) == 7:
                decoded[8] = set(number)
        
        for number in unique:
            if len(number) == 5 and decoded[1].issubset(number):
                decoded[3] = set(number)

        left_line = decoded[8].difference(decoded[3])
        
        for number in unique:
            if len(number) == 6 and decoded[3].issubset(number):
                decoded[9] = set(number)
            if len(number) == 6 and left_line.issubset(number) and decoded[1].issubset(number):
                decoded[0] = set(number)
            if len(number) == 6 and left_line.issubset(number) and not decoded[1].issubset(number):
                decoded[6] = set(number)
            if len(number) == 5 and len(decoded[4].intersection(number)) == 2 and set(number) not in decoded.values():
                decoded[2] = set(number)
            if len(number) == 5 and len(decoded[4].intersection(number)) == 3 and set(number) not in decoded.values():
                decoded[5] = set(number)


        string = ""
        for number in value[1]:
            for k, value in decoded.items():
                if set(number) == value:
                    string += str(k)
        digits.append(int(string))

    print(digits)            



    result2 = sum(digits)
    return result1, result2


# --------------------------------------------------------- # 
import os
from pathlib import Path


curr_dir = Path(__file__).parent

with (curr_dir / "test_input.txt").open() as input:
    assert os.stat(input.fileno()).st_size, "test_input.txt is empty!"
    part1, part2 = main(input)
    part1_expected = 26
    assert part1 == part1_expected, f"Incorrect for test1. Expected: {part1_expected}. Actual: {part1}"
    part2_expected = 61229
    assert part2 == part2_expected, f"Incorrect for test2. Expected: {part2_expected}. Actual: {part2}"

with (curr_dir / "input.txt").open() as input:
    assert os.stat(input.fileno()).st_size, "input.txt is empty!"
    part1, part2 = main(input)
    print(f"PART1: {part1}")
    print(f"PART2: {part2}")
    part1_expected = 272
    assert part1 == part1_expected, f"Incorrect for part1. Expected: {part1_expected}. Actual: {part1}"
    part2_expected = 1007675
    assert part2 == part2_expected, f"Incorrect for part2. Expected: {part2_expected}. Actual: {part2}"

