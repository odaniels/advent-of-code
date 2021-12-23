class Cube:
    def __init__(self, x_range, y_range, z_range):
        self.x_range = x_range
        self.y_range = y_range
        self.z_range = z_range

    def intersection(self, other):
        start_x = max(self.x_range[0], other.x_range[0])
        start_y = max(self.y_range[0], other.y_range[0])
        start_z = max(self.z_range[0], other.z_range[0])
        end_x   = min(self.x_range[1], other.x_range[1])
        end_y   = min(self.y_range[1], other.y_range[1])
        end_z   = min(self.z_range[1], other.z_range[1])
        if end_x >= start_x and end_y >= start_y and end_z >= start_z:
            return Cube([start_x, end_x], [start_y, end_y], [start_z, end_z])
        else:
            return None

    def size(self):
        return (
            (1 + self.x_range[1] - self.x_range[0]) *
            (1 + self.y_range[1] - self.y_range[0]) *
            (1 + self.z_range[1] - self.z_range[0])
        )


def run_commands(lines):
    p_cubes = []
    n_cubes = []
    for line in lines:
        command, raw_coords = line.split(" ")
        x_range, y_range, z_range = [
            [val for val in list(map(int, part[2:].split("..")))] for part in raw_coords.split(",")
        ]
        new_cube = Cube(x_range, y_range, z_range)
        new_p_cubes = [new_cube] if command == "on" else []
        new_n_cubes = []
        while p_cubes:
            p_cube = p_cubes.pop()
            intersection = new_cube.intersection(p_cube)
            if intersection:
                new_n_cubes.append(intersection)
            new_p_cubes.append(p_cube)
        while n_cubes:
            n_cube = n_cubes.pop()
            intersection = new_cube.intersection(n_cube)
            if intersection:
                new_p_cubes.append(intersection)
            new_n_cubes.append(n_cube)
        p_cubes = new_p_cubes
        n_cubes = new_n_cubes

    return sum(cube.size() for cube in p_cubes) - sum(cube.size() for cube in n_cubes)


def main(input):
    lines = [line.strip() for line in input.readlines()]
    result1 = run_commands(lines[:20])
    result2 = run_commands(lines)
    return result1, result2


TEST_EXPECTED = None, 2758514936282235
PUZZLE_EXPECTED = 561032, 1322825263376414