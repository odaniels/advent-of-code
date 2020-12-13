from pathlib import Path
import itertools

curr_dir = Path(__file__).parent
with (curr_dir / "input.txt").open() as input:
    all_numbers = [int(num) for num in input.read().split("\n")]
    end_index = 0
    for index, number in enumerate(all_numbers[25:], start=25):
        if any(a + b == number for a, b in itertools.combinations(all_numbers[index-25:index], 2)):
            continue
        else:
            print("PART 1:", number)
            end_index = index
            break

    for set_size in range(2, end_index):
        for i, _ in enumerate(all_numbers[set_size:end_index], start=set_size):
            _set = all_numbers[i-set_size:i]
            if sum(_set) == number:
                print("PART 2:", min(_set) + max(_set))
                break
