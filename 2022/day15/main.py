from pathlib import Path
from collections import defaultdict

input_file = "input.txt"
#input_file = "test_input.txt"
with (Path(__file__).parent / input_file).open() as input_file:
    lines = [line for line in input_file.read().split("\n")]

sensor_closest = {}
beacons = set()
for line in lines:
    sx = int(line.split("x=")[1].split(",")[0])
    sy = int(line.split("y=")[1].split(":")[0])
    bx = int(line.split("x=")[2].split(",")[0])
    by = int(line.split("y=")[2].split(":")[0])
    sensor_closest[(sx,sy)] = (bx,by)
    beacons.add((bx,by))

sensor_free = {}
for sensor, closest in sensor_closest.items():
    sx, sy = sensor
    bx, by = closest
    manhattan = abs(sx-bx) + abs(sy-by)
    sensor_free[sensor] = manhattan

max_dist = 4000000
for y in range(max_dist):
    spaces = set()
    for sensor, manhattan in sensor_free.items():  
        sx, sy = sensor
        dy = abs(sy - y)
        dx = manhattan - dy
        if dx > 0:
            new_space = (sx - dx, sx + dx)
            intersections = [space for space in spaces if space[0] <= new_space[1] + 1  and space[1] >= new_space[0] - 1]
            for intersection in intersections:
                spaces.remove(intersection)
            intersections.append(new_space)
            final_space = (min(s[0] for s in intersections), max(s[1] for s in intersections))
            spaces.add(final_space)
    if len(spaces) == 2:
        x = max(space[0] for space in spaces) - 1
        print(x * 4000000 + y)
        break
