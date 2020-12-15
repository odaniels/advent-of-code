from pathlib import Path

curr_dir = Path(__file__).parent
with (curr_dir / "input.txt").open() as input:
    next_numbers = {int(n): i + 1 for i, n in enumerate(input.read().split(","))}
    next_number = 0
    for index in range(len(next_numbers) + 1, 30000001):
        curr_number = next_number
        next_number = next_numbers.get(curr_number, 0)
        if next_number:
            next_number = index - next_number
        next_numbers[curr_number] = index
        if (index == 2020):
            print("PART 1:", curr_number)
    print("PART 2:", curr_number)