from pathlib import Path
from collections import Counter, defaultdict, deque 

input_file = "input.txt"
#input_file = "test_input.txt"
with (Path(__file__).parent / input_file).open() as input_file:
    input = input_file.read()

lines = [in_line.split() for in_line in input.split("\n")]

tail = [(0,0) for _ in range(10)] # part1 => range(2)
visited = set()
for direction, steps in lines:
    for i in range(int(steps)):
        x, y = tail[0]
        tail[0] = {
            "U": (x - 1, y),
            "D": (x + 1, y),
            "L": (x, y - 1),
            "R": (x, y + 1),
        }[direction]
        for i in range(1, len(tail)):
            x0, y0 = tail[i-1]
            x1, y1 = tail[i]
            dx = x0 - x1
            dy = y0 - y1
            if abs(dx) > 1 or abs(dy) > 1:
                x1 += dx / abs(dx) if dx else 0
                y1 += dy / abs(dy) if dy else 0
                tail[i] = (x1, y1)
        visited.add(tail[-1])
print(len(visited))
