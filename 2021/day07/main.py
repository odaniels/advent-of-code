def main(input):
    values = [int(in_line) for in_line in input.read().split(",")]
    result1 = min(sum(abs(a - b) for b in values) for a in range(max(values)))
    result2 = min(sum(int(abs(a - b) * (abs(a - b) + 1) / 2) for b in values) for a in range(max(values)))
    return result1, result2


TEST_EXPECTED = 37, 168
PUZZLE_EXPECTED = 336131, 92676646