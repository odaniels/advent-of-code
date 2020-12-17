from pathlib import Path

curr_dir = Path(__file__).parent
with (curr_dir / "input.txt").open() as input:
    data = [[[[c == "#" for c in line] for line in input.read().split("\n")]]]
    for cycle in range(6):
        print(cycle)
        new_data = []
        for w in range(-1, len(data) + 1):
            new_data.append([])
            for z in range(-1, len(data[0]) + 1):
                new_data[w + 1].append([])
                for r in range(-1, len(data[0][0]) + 1):
                    new_data[w + 1][z + 1].append([])
                    for c in range(-1, len(data[0][0][0]) + 1):
                        neighbors = 0
                        for ww in [-1, 0, 1]:
                            for zz in [-1, 0, 1]:
                                for rr in [-1, 0, 1]:
                                    for cc in [-1, 0, 1]:
                                        if (-1 < w + ww < len(data)) and \
                                           (-1 < z + zz < len(data[0])) and \
                                           (-1 < r + rr < len(data[0][0])) and \
                                           (-1 < c + cc < len(data[0][0][0])) and \
                                           data[w + ww][z + zz][r + rr][c + cc]:
                                            neighbors += 1
                        is_active = (-1 < w < len(data)) and \
                                    (-1 < z < len(data[0])) and \
                                    (-1 < r < len(data[0][0])) and \
                                    (-1 < c < len(data[0][0][0])) and \
                                    data[w][z][r][c]
                        if is_active:
                            new_data[w + 1][z + 1][r + 1].append(neighbors in [3, 4])
                        else:
                            new_data[w + 1][z + 1][r + 1].append(neighbors == 3)
        data = new_data.copy()
    print("PART 2", sum(sum(sum(sum(cols) for cols in rows) for rows in fourth) for fourth in data))
