from pathlib import Path
from collections import Counter, defaultdict, deque 

input_file = "input.txt"
#input_file = "test_input.txt"
with (Path(__file__).parent / input_file).open() as input_file:
    input = input_file.read()

lines = [in_line for in_line in input.split("\n")]

grid = {}
for x, row in enumerate(lines):
    for y, val in enumerate(row):
        grid[(x,y)] = int(val)

max_x = max(x for x, y in grid.keys())
max_y = max(y for x, y in grid.keys())

visible, score = 0,0
for pos in grid:
    x, y = pos
    a, b, c, d = 0,0,0,0
    is_visible = False
    for i in range(0,x):
        a += 1
        if grid[(x,y)] <= grid[(x-i-1, y)]:
            break
    else:
        is_visible = True
    for i in range(x,max_x):
        b += 1
        if grid[(x,y)] <= grid[(i+1, y)]:
            break
    else:
        is_visible = True
    for i in range(0,y):
        c += 1
        if grid[(x,y)] <= grid[(x, y-i-1)]:
            break
    else:
        is_visible = True
    for i in range(y,max_y):
        d += 1
        if grid[(x,y)] <= grid[(x, i+1)]:
            break
    else:
        is_visible = True
    
    visible += 1 if is_visible else 0
    score = a*b*c*d if a*b*c*d > score else score

part1, part2 = visible, score

print(part1, part2)
