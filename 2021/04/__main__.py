from pathlib import Path


def main(input):
    draws, *raw_boards = input.read().split("\n\n")
    boards = [[line.split() for line in block.strip().split("\n")] for block in raw_boards]

    wins = {}
    for draw in draws.split(","):
        for b, board in enumerate(boards):
            for r, row in enumerate(board):
                for c, col in enumerate(row):
                    if col == draw:
                        boards[b][r][c] = None
                if all(col == None for col in row) or all(row[r] == None for row in board):
                    if b not in wins:
                        result = sum(sum(int(col) for col in row if col != None) for row in board)
                        wins[b] = int(draw) * result

    return list(wins.values())[0], list(wins.values())[-1]


# --------------------------------------------------------- #

curr_dir = Path(__file__).parent

with (curr_dir / "test_input.txt").open() as input:
    part1, part2 = main(input)
    assert part1 == 4512
    assert part2 == 1924

with (curr_dir / "input.txt").open() as input:
    part1, part2 = main(input)
    assert part1 == 82440
    assert part2 == 20774
    print(f"PART1: {part1}")
    print(f"PART2: {part2}")
