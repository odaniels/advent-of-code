from collections import defaultdict


def main(input):
    start, insertions = input.read().split("\n\n")
    start = start.strip()

    pairs = defaultdict(int)
    for a, b in zip(start[:-1], start[1:]):
        pairs[(a,b)] += 1

    insertion_rules = dict()
    for line in insertions.split("\n"):
        pair, insertion = line.split(" -> ")
        a, b = pair
        insertion_rules[(a, b)] = insertion

    pairs_steps = [pairs]
    for _ in range(40):
        new_pairs = defaultdict(int)
        for pair, count in pairs.items():
            if pair in insertion_rules:
                new_pair1 = (pair[0], insertion_rules[pair])
                new_pairs[new_pair1] += count
                new_pair2 = (insertion_rules[pair], pair[1])
                new_pairs[new_pair2] += count
        pairs = new_pairs
        pairs_steps.append(new_pairs)

    results = []
    for step in pairs_steps:
        letters = defaultdict(int)
        letters[start[-1]] += 1
        for pair, c in step.items():
            first, last = pair
            letters[first] += c
        letter_counts = sorted(letters.values())
        results.append(letter_counts[-1] - letter_counts[0])

    return results[10], results[40]


TEST_EXPECTED = 1588, 2188189693529
PUZZLE_EXPECTED = 2010, 2437698971143