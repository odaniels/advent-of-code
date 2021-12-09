def main(input):
    numbers = [[int(v) for v in line] for line in input.readlines()]
    result1 = None
    result2 = None
    return result1, result2


# --------------------------------------------------------- #
import sys
from pathlib import Path

sys.path.insert(0, '')
from utils.utils import run

run(main, Path(__file__).parent / "test_input.txt", part1_expected=None, part2_expected=None)
run(main, Path(__file__).parent / "input.txt", part1_expected=None, part2_expected=None)