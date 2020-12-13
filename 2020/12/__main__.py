from pathlib import Path
import numpy as np

curr_dir = Path(__file__).parent
pos = (0, 0)
direction = (10, 1)
with (curr_dir / "input.txt").open() as input:
    input_list = [in_line.split("\n")[0] for in_line in input]
    for nu, action in enumerate(input_list):
        act = action[0]
        value = int(action[1:])
        if act == 'N':
            direction = tuple(np.add(direction, np.multiply((0, 1), value)))
        if act == 'S':
            direction = tuple(np.add(direction, np.multiply((0, -1), value)))
        if act == 'E':
            direction = tuple(np.add(direction, np.multiply((1, 0), value)))
        if act == 'W':
            direction = tuple(np.add(direction, np.multiply((-1, 0), value)))
        if act == 'L':
            while value:
                value -= 90
                direction = (-direction[1], direction[0])
        if act == 'R':
            while value:
                value -= 90
                direction = (direction[1], -direction[0])
        if act == 'F':
            pos = tuple(np.add(pos, np.multiply(direction, value)))
        print(action, pos, direction)
        print(abs(pos[0]) + abs(pos[1]))
        
