from pathlib import Path


curr_dir = Path(__file__).parent
with (curr_dir / "input.txt").open() as input:
    values = [in_line.split(" ") for in_line in input]
    x, z, aim = 0, 0, 0
    for command in values:
        direction = command[0]
        steps = int(command[1])
        if direction == "forward":
            x += steps
            z += steps * aim # only for PART2
        if direction == "up":
            # PART1: z -= steps
            aim -= steps
        if direction == "down":
            # PART1: z += steps
            aim += steps

    result = x * z
    # print(f"PART1: {result}")
    print(f"PART2: {result}")

