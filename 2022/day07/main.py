
from pathlib import Path
from collections import Counter 

def main(input):
    lines = [in_line for in_line in input.split("\n")]

    stack = ["/"]
    total_sizes = Counter()
    for line in lines[1:]:
        curr = stack[-1]
        parts = line.split(" ")
        if parts[0] == "$":
            if parts[1] == "cd":
                if parts[2] == "..":
                    stack.pop()
                else:
                    stack.append(curr + "/" + parts[2])
        elif parts[0] != "dir":
            for element in stack:
                total_sizes[element] += int(parts[0])
    
    part1 = sum(value for key, value in total_sizes.items() if value <= 100000)

    needed_space = total_sizes["/"] - 70000000 + 30000000
    part2 = min(value for key, value in total_sizes.items() if value >= needed_space)

    return part1, part2

if __name__ == "__main__": 
    input_file = "input.txt"
    #input_file = "test_input.txt"
    with (Path(__file__).parent / input_file).open() as input:
        print(main(input.read()))