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


TEST_EXPECTED = 4512, 1924
PUZZLE_EXPECTED = 82440, 20774