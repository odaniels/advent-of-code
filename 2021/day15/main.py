from collections import Counter


def valid_neighbors(grid, pos):
    x, y = pos
    neighbors_coords = [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1)
    ]
    return [(_x, _y) for _x, _y in neighbors_coords if (_x, _y) in grid]

def find_path(risk_map, start, end):
    total_risks = Counter()
    for neighbor in valid_neighbors(risk_map, start):
        total_risks[neighbor] += risk_map[neighbor]

    queue = total_risks.copy()
    while queue:
        node, total_risk = queue.most_common()[-1]
        del queue[node]
        if node == end:
            return total_risks[node]
        for neighbor in valid_neighbors(risk_map, node):
            if neighbor in total_risks:
                continue
            else:
                queue[neighbor] = total_risk + risk_map[neighbor]
                total_risks[neighbor] += queue[neighbor]

def main(input):
    numbers = [list(map(int, line.strip())) for line in input.readlines()]
    risk_map = {(x, y): numbers[y][x] for y, row in enumerate(numbers) for x, value in enumerate(row)}
    result1 = find_path(risk_map, (0,0), (len(numbers[0]) - 1, len(numbers) - 1))

    big_map = {}
    scale = 1
    for i in range(scale):
        for j in range(scale):
            for pos, cost in risk_map.items():
                x, y = pos
                big_map[(x + i * len(numbers), y + j * len(numbers))] = 1 + ((cost - 1 + i + j) % 9)

    result2 = find_path(big_map, (0,0), (len(numbers[0]) * scale - 1, len(numbers) * scale - 1))

    return result1, result2


TEST_EXPECTED = 40, 315
PUZZLE_EXPECTED = 386, 2806