from pathlib import Path

curr_dir = Path(__file__).parent
with (curr_dir / "input.txt").open() as input:
    input_list = [in_line.split("\n")[0] for in_line in input]
    valid = 0
    for line in input_list:
        parts = line.split(" ")
        min, max = parts[0].split("-")
        letter = parts[1][0]
        code = parts[2]
        is_valid = (code[int(min) - 1] == letter) != (code[int(max) - 1] == letter)
        valid = valid + 1 if is_valid else valid
    print(valid)