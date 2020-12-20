from pathlib import Path
from math import sqrt


class Tile:
    def __init__(self, input):
        self.id = int(input.split("\n")[0][5:-1])
        self.lines = input.split("\n")[1:]
        self.matches = set()
        self.reset_sides()
    
    def reset_sides(self):
        self.sides = [
            self.lines[0], # TOP
            "".join([line[-1] for line in self.lines]), # RIGHT
            self.lines[-1], # BOTTOM
            "".join([line[0] for line in self.lines]), # LEFT
        ]

    def __str__(self):
        return str(self.id)

    def add_match(self, matching_tile):
        if set(self.sides).intersection(set(matching_tile.sides)):
            self.matches.add(matching_tile.id)
            matching_tile.matches.add(self.id) 
        else:
            reversed_sides = {side[::-1] for side in set(self.sides)}
            if reversed_sides.intersection(set(matching_tile.sides)):
                self.matches.add(matching_tile.id)
                matching_tile.matches.add(self.id)

    def get_match_info(self, matching_tile):
        normal_match = set(self.sides).intersection(set(matching_tile.sides))
        if normal_match:
            return False, self.sides.index(next(iter(normal_match)))
        else:
            reversed_sides = [side[::-1] for side in self.sides]
            normal_match = set(reversed_sides).intersection(set(matching_tile.sides))
            if normal_match:
                return True, reversed_sides.index(next(iter(normal_match)))

    def rotate(self):
        new_lines = []
        for i in range(len(self.lines)):
            new_lines.append("".join(line[-1 - i] for line in self.lines))
        self.lines = new_lines
        self.reset_sides()
    
    def flip_up_down(self):
        self.lines = self.lines[::-1]
        self.reset_sides()
        
    def flip_left_right(self):
        self.rotate()
        self.flip_up_down()
        self.rotate()
        self.rotate()
        self.rotate()


curr_dir = Path(__file__).parent
with (curr_dir / "input.txt").open() as input:
    tile_list = [Tile(tile) for tile in input.read().split("\n\n")]
    tile_list = {tile.id: tile for tile in tile_list}
    
    # Find matches
    for tile in tile_list.values():
        for matching_tile in tile_list.values():
            if tile.id != matching_tile.id:
                tile.add_match(matching_tile)
    
    # Identify corners 
    corners = {key: tile for key, tile in tile_list.items() if len(tile.matches) == 2}
    sides = {key: tile  for key, tile in tile_list.items() if len(tile.matches) <= 3}
    middle = {key: tile  for key, tile in tile_list.items() if len(tile.matches) == 4}
    part1 = 1
    for corner in corners.values():
        part1 *= corner.id
    print("PART 1:", part1)

    # Place on grid
    size = int(sqrt(len(tile_list)))
    grid = []
    for rid in range(size):
        grid.append([])
        row = grid[rid]
        for cid in range(size):
            if rid == 0:
                if cid == 0:
                    row.append(next(iter(corners)))
                elif cid == 1:
                    row.append(next(iter(tile_list[row[0]].matches)))
                else:
                    options = tile_list[row[cid-1]].matches
                    options = set(sides.keys()).intersection(options)
                    options.remove(row[cid-2])
                    row.append(next(iter(options)))
            elif rid == 1:
                options = tile_list[grid[rid-1][cid]].matches
                options = options - set(grid[rid-1])
                row.append(next(iter(options)))
            else:
                options = tile_list[grid[rid-1][cid]].matches
                options = options - set(grid[rid-1]) - set(grid[rid-2])
                row.append(next(iter(options)))

    # Rotate and flip
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if r == 0 and c == 0:
                _, side_idx = tile_list[col].get_match_info(tile_list[row[c + 1]])
                num_rotations = (side_idx + 3) % 4
                for _ in range(num_rotations):
                    tile_list[col].rotate()
                _, side_idx = tile_list[col].get_match_info(tile_list[grid[r+1][c]])
                if side_idx != 2:
                    tile_list[col].flip_up_down()
            elif r == 0:
                _, side_idx = tile_list[col].get_match_info(tile_list[row[c - 1]])
                num_rotations = (side_idx + 1) % 4
                for _ in range(num_rotations):
                    tile_list[col].rotate()
                rev, _ = tile_list[col].get_match_info(tile_list[row[c - 1]])
                if rev:
                    tile_list[col].flip_up_down()
            else:
                _, side_idx = tile_list[col].get_match_info(tile_list[grid[r - 1][c]])
                num_rotations = side_idx % 4
                for _ in range(num_rotations):
                    tile_list[col].rotate()
                rev, _ = tile_list[col].get_match_info(tile_list[grid[r - 1][c]])
                if rev:
                    tile_list[col].flip_left_right()

    grid = [[[line[1:-1] for line in tile_list[col].lines[1:-1]] for col in row] for row in grid]
    image = []
    for row in grid:
        for i in range(8):
            row_str = ""
            for col in row:
                row_str += col[i]
            image.append(row_str)

    # Find sea monsters
    image = Tile("\n".join(["Tile 0:"] + image))
    mask = [
        "..................O.",
        "O....OO....OO....OOO",
        ".O..O..O..O..O..O...",
    ]
    mask_idx = [[idx for idx, c in enumerate(line) if c == "O"] for line in mask]
    
    sea_monsters = []
    image.flip_up_down()
    for i in range(4):
        image.rotate()
        for r, row in enumerate(image.lines):
            for c, col in enumerate(row):
                try:
                    if all(all(image.lines[r + mr][c + mc] == "#" for _, mc in enumerate(mrow)) for mr, mrow in enumerate(mask_idx)):
                        sea_monsters.append((r, c))
                except IndexError:
                    pass
        if sea_monsters:
            break

    all_squares = sum(sum(c == "#" for c in row) for row in image.lines)
    monster_squares = 15 * len(sea_monsters)
    print("PART 2:", all_squares - monster_squares)


