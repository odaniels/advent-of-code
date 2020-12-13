from pathlib import Path

with (Path(__file__).parent / "input.txt").open() as input:
    groups = input.read().split("\n\n")
    all_sets_per_group = [[set(line) for line in group.split("\n")] for group in groups]

    part1 = sum([len(set.union(*all_sets)) for all_sets in all_sets_per_group])
    part2 = sum([len(set.intersection(*all_sets)) for all_sets in all_sets_per_group])
    
    print("PART1:", part1)
    print("PART2:", part2)