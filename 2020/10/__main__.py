from pathlib import Path
import itertools

curr_dir = Path(__file__).parent
with (curr_dir / "input.txt").open() as input:
    all_adapters = [0] + [int(num) for num in input.read().split("\n")]
    all_adapters.sort()
    all_adapters += [max(all_adapters) ]
    diffs = [adapter - all_adapters[i-1] for i, adapter in enumerate(all_adapters[1:], start=1)]
    ones = sum(diff == 1 for diff in diffs)
    trees = sum(diff == 3 for diff in diffs) + 1
    print("PART 1:", ones * trees)
    
    nodes = []
    adapters_in_next_node = 0
    for diff in diffs:
        if diff not in [0, 3]:
            adapters_in_next_node += 1
        else:
            nodes.append(adapters_in_next_node)
            adapters_in_next_node = 0
    
    combinations = 1
    for node in nodes:
        if node and node != 4:
            combinations *= pow(2, node - 1) # all combinations when at least last is used
        if node == 4:
            combinations *= pow(2, node - 1) - 1 # at least one except last must be used

    print("PART 2:", combinations)
