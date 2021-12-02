from pathlib import Path
import sys

sys.setrecursionlimit(2000)


curr_dir = Path(__file__).parent
with (curr_dir / "input.txt").open() as input:

    def get_position(values):
        if not values:
            return 0, 0, 0
        direction, steps = values[-1].split(" ")
        x, z, aim = get_position(values[:-1])
        if direction == "forward":
            return (x + int(steps)), (z + int(steps) * aim), aim
        if direction == "up":
            return x, z, (aim - int(steps))
        if direction == "down":
            return x, z, (aim + int(steps))
    x, z, aim = get_position(input.readlines())

    print(f"PART1: {x * aim}")
    print(f"PART2: {x * z}")

