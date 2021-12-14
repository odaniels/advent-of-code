from collections import Counter


def main(input):
    start, insertions = input.read().split("\n\n")
    pairs = Counter((a,b) for a, b in zip(start.strip()[:-1], start.strip()[1:]))
    rules = {(line[0], line[1]): line[-1] for line in insertions.split("\n")}

    pair_steps = [pairs]
    for i in range(40):
        new_pairs = Counter()
        for pair, count in pair_steps[i].items():
            if pair in rules:
                new_pairs[(pair[0], rules[pair])] += count
                new_pairs[(rules[pair], pair[1])] += count
        pair_steps.append(new_pairs)

    results = []
    for step in pair_steps:
        letters = Counter([start[0]])
        for pair, count in step.items():
            letters[pair[1]] += count
        results.append(letters.most_common()[0][1] - letters.most_common()[-1][1])

    return results[10], results[40]


TEST_EXPECTED = 1588, 2188189693529
PUZZLE_EXPECTED = 2010, 2437698971143