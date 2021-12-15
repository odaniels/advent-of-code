import heapq


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
    visited = set()
    queue = [(0, start)]
    while queue:
        total_risk, node = heapq.heappop(queue)
        if node == end:
            return total_risk
        for neighbor in valid_neighbors(risk_map, node):
            if neighbor in visited:
                continue
            else:
                visited.add(neighbor)
                heapq.heappush(queue, (total_risk + risk_map[neighbor], neighbor))

def main(input):
    numbers = [list(map(int, line.strip())) for line in input.readlines()]
    risk_map = {(x, y): numbers[y][x] for y, row in enumerate(numbers) for x, value in enumerate(row)}
    result1 = find_path(risk_map, (0,0), (len(numbers[0]) - 1, len(numbers) - 1))

    big_map = {}
    scale = 5
    for i in range(scale):
        for j in range(scale):
            for pos, cost in risk_map.items():
                x, y = pos
                big_map[(x + i * len(numbers), y + j * len(numbers))] = 1 + ((cost - 1 + i + j) % 9)

    result2 = find_path(big_map, (0,0), (len(numbers[0]) * scale - 1, len(numbers) * scale - 1))

    return result1, result2


TEST_EXPECTED = 40, 315
PUZZLE_EXPECTED = 386, 2806