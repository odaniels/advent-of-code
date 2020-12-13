from pathlib import Path

curr_dir = Path(__file__).parent
with (curr_dir / "input.txt").open() as input:
    input_list = [in_line.split("\n")[0] for in_line in input]
    line_length = len(input_list[0])
    all_trees_encounters = 1
    for side, down in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        indexes = [(side * i) % line_length for i, _ in enumerate(input_list[::down])]
        encounters = [line[index] for index, line in zip(indexes, input_list[::down])]
        trees = sum(c == '#' for c in encounters)
        all_trees_encounters = all_trees_encounters * trees
    print(all_trees_encounters)