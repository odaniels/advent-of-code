from pathlib import Path


curr_dir = Path(__file__).parent
with (curr_dir / "input.txt").open() as input:
    lines = [line.strip() for line in input.readlines()]
    boards = [[line.split() for line in lines[6*i+2:6*i+7]] for i in range(int(len(lines[1:])/6))]

    wins = {}
    for draw in lines[0].split(","):
        for b, board in enumerate(boards):
            for r, row in enumerate(board):
                for c, col in enumerate(row):
                    if col == draw:
                        boards[b][r][c] = None
                if all(col == None for col in row) or all(row[r] == None for row in board):
                    if b not in wins:
                        result = sum(sum(int(col) for col in row if col != None) for row in board)
                        wins[b] = int(draw) * result

    print(f"PART1: {list(wins.values())[0]}")
    print(f"PART2: {list(wins.values())[-1]}")

