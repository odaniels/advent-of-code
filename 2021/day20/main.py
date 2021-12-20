def get_binary(grid, pos, padding):
    x, y = pos
    neighbors_coords = [
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
        (x - 1, y),
        (x, y),
        (x + 1, y),
        (x - 1, y + 1),
        (x, y + 1),
        (x + 1, y + 1)
    ]
    binary = "".join([str(grid[(_x, _y)] if (_x, _y) in grid else padding) for _x, _y in neighbors_coords])
    return int(binary, 2)


def main(input):
    algorithm, input_image = input.read().split("\n\n")
    algorithm = algorithm.strip()

    image = {
        (x,y): int(c == "#")
        for y, row in enumerate(input_image.split("\n"))
        for x, c in enumerate(row.strip())
    }

    result = {}
    padding = 0
    for i in range(50):
        new_image = {}
        all_x = [x for x, y in image.keys()]
        all_y = [y for x, y in image.keys()]
        min_x, max_x = min(all_x) - 1, max(all_x) + 1
        min_y, max_y = min(all_y) - 1, max(all_y) + 1
        for x in range(1 + max_x - min_x):
            xx = x + min_x
            for y in range(1 + max_y - min_y):
                yy = y + min_y
                index = get_binary(image, (xx, yy), padding)
                new_image[(xx, yy)] = int(algorithm[index] == "#")
        image = new_image
        padding = int(algorithm[int("".join(9*[str(padding)]), 2)] == "#")
        result[i+1] = sum(image.values())

    result1 = result[2]
    result2 = result[50]

    return result1, result2


TEST_EXPECTED = 35, 3351
PUZZLE_EXPECTED = 5846, 21149