import os
from datetime import datetime


def run(func, input_file, part1_expected=None, part2_expected=None, run_assert=True):
    with input_file.open() as input:
        assert os.stat(input.fileno()).st_size, "test_input.txt is empty!"
        start = datetime.now()
        parts = func(input)
        end = datetime.now()

        if run_assert:
            print(f"\n####### Results for {input_file.name}")
            print(f"Execution time: {end-start}")
            for i, part in enumerate(parts):
                print(f"PART {i+1}: {part}")
            if part1_expected is not None:
                assert parts[0] == part1_expected, f"Incorrect for test1. Expected: {part1_expected}. Actual: {parts[0]}"
            if part2_expected is not None:
                assert parts[1] == part2_expected, f"Incorrect for test2. Expected: {part2_expected}. Actual: {parts[1]}"

        return part1_expected == parts[0], part2_expected == parts[1], end - start

