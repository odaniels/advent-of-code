from pathlib import Path
import string


input_file = "input.txt"
#input_file = "test_input.txt"
grid = {}
with (Path(__file__).parent / input_file).open() as input_file:
    for x, row in enumerate(input_file.read().split("\n")):
        for y, col in enumerate(row):
            if col == "S":
                S = (x, y)
                grid[(x, y)] = string.ascii_lowercase.index("a")
            elif col == "E":
                E = (x, y)
                grid[(x, y)] = string.ascii_lowercase.index("z")
            else:
                grid[(x, y)] = string.ascii_lowercase.index(col)


def solve(queue: list, grid: dict):
    visited = { pos: steps for pos, steps in queue}
    while queue:
        queue.sort(key=lambda x: -x[1])
        pos, steps = queue.pop()
        if pos == E:
            return steps
        for move in [(1,0), (-1,0), (0,1), (0,-1)]:
            dx, dy = move
            x, y = pos
            new_pos = (x+dx, y+dy)
            if new_pos in visited:
                continue
            if new_pos not in grid:
                continue
            if grid[new_pos] > grid[pos] + 1:
                continue
            queue.append((new_pos, steps+1))
            visited[new_pos] = steps + 1


part1 = solve([(S, 0)], grid)
part2 = solve([(pos, 0) for pos, height in grid.items() if height == 0], grid)
print(part1, part2)
