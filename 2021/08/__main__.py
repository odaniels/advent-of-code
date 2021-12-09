def main(input):
    encoded_lines = [[b.strip().split() for b in a.split("|")] for a in input.readlines()]

    decoded_output = []
    for encoded in encoded_lines:
        decoded = {}
        uniques, output = encoded

        decoded[1] = next(n for n in uniques if len(n) == 2)
        decoded[7] = next(n for n in uniques if len(n) == 3)
        decoded[4] = next(n for n in uniques if len(n) == 4)
        decoded[8] = next(n for n in uniques if len(n) == 7)
        decoded[3] = next(n for n in uniques if len(n) == 5 and set(decoded[1]).issubset(n))
        decoded[9] = next(n for n in uniques if len(n) == 6 and set(decoded[3]).issubset(n))

        left_line = set(decoded[8]).difference(decoded[3])
        decoded[0] = next(n for n in uniques if len(n) == 6 and left_line.issubset(n) and set(decoded[1]).issubset(n))
        decoded[6] = next(n for n in uniques if len(n) == 6 and left_line.issubset(n) and not set(decoded[1]).issubset(n))
        decoded[2] = next(n for n in uniques if len(n) == 5 and len(set(decoded[4]).intersection(n)) == 2)
        decoded[5] = next(n for n in uniques if len(n) == 5 and len(set(decoded[6]).intersection(n)) == 5)

        out_digit = int("".join([str(next(k for k, value in decoded.items() if set(n) == set(value))) for n in output]))
        decoded_output.append(out_digit)

    result1 = sum(sum(len(encoded) in [2, 3, 4, 7] for encoded in line[1]) for line in encoded_lines)
    result2 = sum(decoded_output)

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

