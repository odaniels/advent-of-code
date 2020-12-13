from pathlib import Path

with (Path(__file__).parent / "input.txt").open() as input:

    all_ids = [int(line.replace("F","0").replace("B","1").replace("L","0").replace("R","1"), 2) 
               for line in input.read().split("\n")]

    print("PART1:", max(all_ids))
    print("PART2:", next(i for i in range(min(all_ids), max(all_ids)) if i not in all_ids))