from pathlib import Path


input_file = "input.txt"
#input_file = "test_input.txt"
with (Path(__file__).parent / input_file).open() as input_file:
    lines = [line for line in input_file.read().split("\n")]

rocks = set()
for line in lines:
    nodes = []
    for coord in line.split(" -> "):
        x, y = [int(c) for c in coord.split(",")]
        nodes.append((x,y))
    for start, end in zip(nodes[:-1], nodes[1:]):
        dx, dy = end[0] - start[0], end[1] - start[1]
        for j in range(abs(dx)+1):
            step = j if dx > 0 else -j
            rocks.add((start[0]+step, start[1]))
        for j in range(abs(dy)+1):
            step = j if dy > 0 else -j
            rocks.add((start[0], start[1]+step))

sand = set()
max_y = max(y for x, y in rocks)
finished = False
while True:
    if finished:
        break
    curr = (500, 0)
    while True:
        next_curr = (curr[0], curr[1]+1)
        if next_curr not in rocks and next_curr not in sand and next_curr[1] != max_y+2:
            curr = next_curr
            continue
        next_curr = (curr[0]-1, curr[1]+1)
        if next_curr not in rocks and next_curr not in sand and next_curr[1] != max_y+2:
            curr = next_curr
            continue
        next_curr = (curr[0]+1, curr[1]+1)
        if next_curr not in rocks and next_curr not in sand and next_curr[1] != max_y+2:
            curr = next_curr
            continue
        sand.add(curr)
        if curr == (500,0):
            finished = True
        break

print(len(sand))




        