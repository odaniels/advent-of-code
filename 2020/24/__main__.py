from pathlib import Path


DIR_OFFSETS = {
    "e":  (0, 2), "se": (-1, 1), "ne": (1, 1),
    "w":  (0, -2), "sw": (-1, -1), "nw": (1, -1)
}
            

black_tiles = set()
curr_dir = Path(__file__).parent
with (curr_dir / "input.txt").open() as input:
    lines = [list(line) for line in input.read().split("\n")]
    directions = []
    for line in lines:
        pos = (0, 0)
        while line:
            direction = line.pop(0)
            if direction in ["n","s"]:
                direction += line.pop(0)
            offset = DIR_OFFSETS[direction]
            pos = (pos[0] + offset[0], pos[1] + offset[1])
        else:
            if pos in black_tiles:
                black_tiles.remove(pos)
            else:
                black_tiles.add(pos)

print("PART 1:", len(black_tiles))
    
new_black_tiles = set()
for i in range(100):
    for tile in black_tiles:
        neighbors = [(tile[0] + d_o[0], tile[1] + d_o[1]) for d_o in DIR_OFFSETS.values()]
        white_neighbors = [neighbor for neighbor in neighbors if neighbor not in black_tiles]
        if len(white_neighbors) in [4, 5]:
            new_black_tiles.add(tile)
        for white in white_neighbors:
            neighbors_to_white = [(white[0] + d_o[0], white[1] + d_o[1]) for d_o in DIR_OFFSETS.values()]
            black_neighbors = [neighbor for neighbor in neighbors_to_white if neighbor in black_tiles]
            if len(black_neighbors) == 2:
                new_black_tiles.add(white)
    black_tiles = new_black_tiles.copy()
    new_black_tiles = set()

print("PART 2:", len(black_tiles))
