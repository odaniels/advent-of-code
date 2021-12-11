from collections import defaultdict


def _range(first, last):
    step = 1 if first < last else -1
    return range(first, last + step, step)


def find_overlap(line_points, allow_diagonals):
    points = defaultdict(int)
    for line in line_points:
        x1, y1 = [int(coord) for coord in line[0].split(",")]
        x2, y2 = [int(coord) for coord in line[1].split(",")]
        x_range = _range(x1, x2)
        y_range = _range(y1, y2)
        if x1 == x2:
            coords = zip([x1] * len(y_range), y_range)
        elif y1 == y2:
            coords = zip(x_range, [y1] * len(x_range))
        elif allow_diagonals and len(x_range) == len(y_range):
            coords = zip(x_range, y_range)
        else:
            continue

        for coord in coords:
            points[coord] += 1

    return sum(v >= 2 for k,v in points.items())


def main(input):
    line_points = [in_line.split(" -> ") for in_line in input.readlines()]
    return find_overlap(line_points, False), find_overlap(line_points, True)


TEST_EXPECTED = 5, 12
PUZZLE_EXPECTED = 4421, 18674