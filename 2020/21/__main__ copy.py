import fileinput as fi
from collections import Counter
import itertools as it
from pathlib import Path

all_foods = set()
times = Counter()

pos = {}

curr_dir = Path(__file__).parent
rows = []
with (curr_dir / "input.txt").open() as input:
    rows = input.read().split("\n")

for line in rows:
    a, b = line.split(" (contains ")
    foods = set(a.split())
    algs = set(b[:-1].split(", "))

    all_foods |= foods
    times.update(foods)

    for alg in algs:
        if alg not in pos:
            pos[alg] = foods.copy()
        else:
            pos[alg] &= foods

bad = set(it.chain.from_iterable(pos.values()))
print(len(all_foods - bad))

print( sum(sum(ingredient in row for row in rows) for ingredient in all_foods - bad))