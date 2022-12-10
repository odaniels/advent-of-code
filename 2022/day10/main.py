from pathlib import Path


with (Path(__file__).parent / "input.txt").open() as input_file:
    lines = [in_line for in_line in input_file.read().split("\n")]

string = ""
signal_values = []
X = 1
for line in lines:
    for part in line.split():
        string += "\n" if len(signal_values) % 40 == 0 else ""
        string += "#" if abs(len(signal_values) % 40 - X) <= 1 else " "
        signal_values.append(X * (1 + len(signal_values)))
        X += 0 if part in ["noop", "addx"] else int(part)

print(sum(signal_values[i-1] for i in [20, 60, 100, 140, 180, 220]))
print(string)