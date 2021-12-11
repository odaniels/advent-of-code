import sys

sys.setrecursionlimit(2000)

def main(input):
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
    return x * aim, x * z

TEST_EXPECTED = 150, 900
PUZZLE_EXPECTED = 1670340, 1954293920