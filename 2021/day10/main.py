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


TEST_EXPECTED = 26397, 288957
PUZZLE_EXPECTED = 345441, 3235371166