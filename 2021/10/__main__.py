def main(input):
    braces = [[c for c in line.strip()] for line in input.readlines()]
    errors = []
    incomplete = []

    for brace_line in braces:
        open_braces = []
        for brace in brace_line:
            if brace in ["<", "(", "[", "{"]:
                open_braces.append(brace)
                continue
            last_open = open_braces.pop()
            if brace == ">" and last_open == "<":
                continue
            if brace == "]" and last_open == "[":
                continue
            if brace == ")" and last_open == "(":
                continue
            if brace == "}" and last_open == "{":
                continue
            errors.append(brace)
            break
        else:
            incomplete.append(open_braces)

    result1 = (sum(3 for error in errors if error == ")") +
               sum(57 for error in errors if error == "]") +
               sum(1197 for error in errors if error == "}") +
               sum(25137 for error in errors if error == ">"))

    scores = []
    brace_values = { "(": 1, "[": 2, "{": 3, "<": 4 }
    for line in incomplete:
        score = 0
        while line:
            score = score * 5 + brace_values[line.pop()]

        scores.append(score)
    result2 = list(reversed(sorted(scores)))[int(len(scores)/2)]
    return result1, result2


# --------------------------------------------------------- #
import sys
from pathlib import Path

sys.path.insert(0, '')
from utils.utils import run

run(main, Path(__file__).parent / "test_input.txt", part1_expected=26397, part2_expected=288957)
run(main, Path(__file__).parent / "input.txt", part1_expected=345441, part2_expected=3235371166)