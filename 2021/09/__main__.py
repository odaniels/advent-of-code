def valid_neighbors(height_map, pos):
    x, y = pos
    neighbors_coords = [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
    return [(_x, _y) for _x, _y in neighbors_coords if (_x, _y) in height_map]


def main(input):
    values = [[int(val) for val in in_line.strip()] for in_line in input.readlines()]
    height_map = {(x, y): values[y][x] for y, row in enumerate(values) for x, value in enumerate(row)}

    low_points = {
        pos: height for pos, height in height_map.items()
        if all(height_map[neighbor] > height for neighbor in valid_neighbors(height_map, pos))
    }
    result1 = sum(1 + height for height in low_points.values())

    basins = [set([pos]) for pos in low_points.keys()]
    for _ in range(9):
        for basin in basins:
            for pos in basin.copy():
                basin |= set(pos for pos in valid_neighbors(height_map, pos) if height_map[pos] != 9)
    a, b, c, *_ = reversed(sorted([len(basin) for basin in basins]))
    result2 = a * b * c

    return result1, result2


# --------------------------------------------------------- #
import os
from pathlib import Path


curr_dir = Path(__file__).parent

with (curr_dir / "test_input.txt").open() as input:
    assert os.stat(input.fileno()).st_size, "test_input.txt is empty!"
    part1, part2 = main(input)
    part1_expected = 15
    assert part1 == part1_expected, f"Incorrect for test1. Expected: {part1_expected}. Actual: {part1}"
    part2_expected = 1134
    assert part2 == part2_expected, f"Incorrect for test2. Expected: {part2_expected}. Actual: {part2}"

with (curr_dir / "input.txt").open() as input:
    assert os.stat(input.fileno()).st_size, "input.txt is empty!"
    part1, part2 = main(input)
    print(f"PART1: {part1}")
    print(f"PART2: {part2}")
    part1_expected = 452
    assert part1 == part1_expected, f"Incorrect for part1. Expected: {part1_expected}. Actual: {part1}"
    part2_expected = 1263735
    assert part2 == part2_expected, f"Incorrect for part2. Expected: {part2_expected}. Actual: {part2}"

