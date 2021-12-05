from pathlib import Path


def _range(first, last):
    step = 1 if first < last else -1
    return range(first, last + step, step)


def find_overlap(line_points, allow_diagonals):
    points = {}
    for line in line_points:
        x1, y1 = [int(coord) for coord in line[0].split(",")]
        x2, y2 = [int(coord) for coord in line[1].split(",")]
        if x1 == x2:
            y = _range(y1, y2)
            coords = zip([x1] * len(y), y)
        elif y1 == y2:
            x = _range(x1, x2)
            coords = zip(x, [y1] * len(x))
        elif allow_diagonals and (abs(x1 - x2) == abs(y1 - y2)):
            coords = zip(_range(x1, x2), _range(y1, y2))
        else:
            continue

        for coord in coords:
            if str(coord) in points:
                points[str(coord)] += 1
            else:
                points[str(coord)] = 1
    
    return sum(v >= 2 for k,v in points.items())


def main(input):
    line_points = [in_line.split(" -> ") for in_line in input.readlines()]
    return (
        find_overlap(line_points, False),
        find_overlap(line_points, True)
    )


# --------------------------------------------------------- # 

curr_dir = Path(__file__).parent

with (curr_dir / "test_input.txt").open() as input:
    part1, part2 = main(input)
    assert part1 == 5
    assert part2 == 12

with (curr_dir / "input.txt").open() as input:
    part1, part2 = main(input)
    assert part1 == 4421
    assert part2 == 18674
    print(f"PART1: {part1}")
    print(f"PART2: {part2}")

