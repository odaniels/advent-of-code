from pathlib import Path

curr_dir = Path(__file__).parent
with (curr_dir / "input.txt").open() as input:
    input_list = [int(in_line.split("\n")[0]) for in_line in input]
    for i, value in enumerate(input_list):
        for j, other_value in enumerate(input_list[i+1:]):
            for third_value in input_list[i+j+1:]:
                if value + other_value + third_value == 2020:
                    print(value, other_value, third_value, value * other_value * third_value)