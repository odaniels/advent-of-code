def draw(dots):
    for y in range(6):
        line = ""
        for x in range(40):
            if (x, y) in dots:
                line += "█"
            else:
                line += " "
        print(line)
    print()


def main(input):
    coord_in, fold_in = input.read().split("\n\n")
    dots = set([tuple(map(int, line.strip().split(","))) for line in coord_in.split("\n")])
    results = [dots]

    for fold in fold_in.split("\n"):
        fold_axis, fold_coord = fold.split(" ")[-1].split("=")
        fold_coord = int(fold_coord)
        new_dots = set()

        for dot in dots:
            if fold_axis == "x":
                new_dots |= {(2 * fold_coord - dot[0], dot[1])} if dot[0] > fold_coord else {dot}
            if fold_axis == "y":
                new_dots |= {(dot[0], 2 * fold_coord - dot[1])} if dot[1] > fold_coord else {dot}

        dots = new_dots
        results.append(dots)

    result1 = len(results[1])
    result2 = len(results[-1])  # Not actual result, only for unit test
    # draw(results[-1])

    return result1, result2


TEST_EXPECTED = 17, 16
PUZZLE_EXPECTED = 729, 100