def main(input):
    fish_ages = [int(age) for age in input.read().split(",")]
    fish_sums = [sum(int(age) == idx for age in fish_ages) for idx in range(9)]

    total = [sum(fish_sums)]
    for _ in range(256):
        new_fishes = fish_sums[0]
        fish_sums = fish_sums[1:] + [new_fishes]
        fish_sums[6] += new_fishes
        total.append(sum(fish_sums))

    return total[80], total[256]


TEST_EXPECTED = 5934, 26984457539
PUZZLE_EXPECTED = 355386, 1613415325809