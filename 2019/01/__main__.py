from pathlib import Path


def get_fuel(mass):
    new_fuel = int(mass / 3) - 2
    if new_fuel <= 0:
        return 0
    else:
        return new_fuel + get_fuel(new_fuel)

curr_dir = Path(__file__).parent
with (curr_dir / "input.txt").open() as input:
    masses = [int(in_line.split("\n")[0]) for in_line in input]
    fuel_sum = sum(int(mass / 3) - 2 for mass in masses)
    print(f"PART1: {fuel_sum}")
    new_fuel_sum = sum(get_fuel(mass) for mass in masses)
    print(f"PART2: {new_fuel_sum}")

