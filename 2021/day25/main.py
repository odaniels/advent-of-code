def main(input):
    lines = input.readlines()
    width, height =  len(lines[0].strip()), len(lines)
    down = set()
    right = set()

    for y, row in enumerate(lines):
        for x, col in enumerate(row.strip()):
            if col == "v":
                down.add((x, y))
            if col == ">":
                right.add((x,y))

    result1 = None
    for i in range(10000):
        has_moved = 0
        new_down = set()
        new_right = set()
        for cucumber in right:
            x, y = cucumber
            new_pos = ((x + 1) % width, y)
            if new_pos in down or new_pos in right:
                new_right.add(cucumber)
            else:
                new_right.add(new_pos)
                has_moved += 1
        for cucumber in down:
            x, y = cucumber
            new_pos = (x, (y + 1) % height)
            if new_pos in down or new_pos in new_right:
                new_down.add(cucumber)
            else:
                new_down.add(new_pos)
                has_moved += 1
        if not has_moved:
            result1 = i+1
            break
        else:
            down = new_down
            right = new_right

    result2 = None

    return result1, result2


TEST_EXPECTED = 58, None
PUZZLE_EXPECTED = 453, None