def valid_neighbors(grid, pos):
    x, y = pos
    neighbors_coords = [
        (x + 1, y),
        (x + 1, y + 1),
        (x + 1, y - 1),
        (x - 1, y),
        (x - 1, y + 1),
        (x - 1, y - 1),
        (x, y + 1),
        (x, y - 1)
    ]
    return [(_x, _y) for _x, _y in neighbors_coords if (_x, _y) in grid]

def main(input):
    numbers = [list(map(int, line.strip())) for line in input.readlines()]
    energy = {(x, y): numbers[y][x] for y, row in enumerate(numbers) for x, value in enumerate(row)}

    result1, result2 = 0, 0
    for step in range(1000):
        flashes = []
        flashed = []
        for pos in energy:
            energy[pos] += 1
            if energy[pos] == 10:
                flashes.append(pos)
        while flashes:
            flash = flashes.pop()
            flashed.append(flash)
            for pos in valid_neighbors(energy, flash):
                energy[pos] += 1
                if energy[pos] == 10:
                    flashes.append(pos)
        for pos in flashed:
            energy[pos] = 0
            if step < 100:
                result1 += 1
        if not any(energy.values()):
            result2 = step + 1
            break

    return result1, result2


# --------------------------------------------------------- #
import sys
from pathlib import Path

sys.path.insert(0, '')
from utils.utils import run

run(main, Path(__file__).parent / "test_input.txt", part1_expected=1656, part2_expected=195)
run(main, Path(__file__).parent / "input.txt", part1_expected=1743, part2_expected=364)