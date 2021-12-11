def main(input):
    values = [int(in_line) for in_line in input]

    def window_sum_increases(window):
        window_sums = [sum(values[i:i + window]) for i in range(len(values) + 1 - window)]
        return sum(b < a for a, b in zip(window_sums[1:], window_sums[:-1]))

    return window_sum_increases(1), window_sum_increases(3)


TEST_EXPECTED = 7, 5
PUZZLE_EXPECTED = 1709, 1761