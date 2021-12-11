def main(input):
    bit_values = [[int(char) for char in line.strip()] for line in input.readlines()]
    middle = len(bit_values) / 2
    bit_sums = [sum(values) for values in zip(*bit_values)]
    gamma = int("".join(["1" if bit > middle else "0" for bit in bit_sums]), 2)
    epsilon = int("".join(["1" if bit < middle else "0" for bit in bit_sums]), 2)
    result1 = gamma * epsilon

    ox_values = bit_values.copy()
    for idx in range(len(ox_values[0])):
        if len(ox_values) == 1:
            break
        middle = len(ox_values) / 2
        filter_value = 1 if sum(line[idx] for line in ox_values) >= middle else 0
        ox_values = [line for line in ox_values if line[idx] == filter_value]

    co_values = bit_values.copy()
    for idx in range(len(co_values[0])):
        if len(co_values) == 1:
            break
        middle = len(co_values) / 2
        filter_value = 1 if sum(line[idx] for line in co_values) < middle else 0
        co_values = [line for line in co_values if line[idx] == filter_value]

    oxygen = int("".join(str(v) for v in ox_values[0]), 2)
    co2 = int("".join(str(v) for v in co_values[0]), 2)
    result2 = oxygen * co2

    return result1, result2


TEST_EXPECTED = 198, 230
PUZZLE_EXPECTED = 2743844, 6677951