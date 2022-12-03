from pathlib import Path

def main(input):
    lines = [in_line for in_line in input.split("\n")]
    prio = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    part1 = 0
    for line in lines:
        length = int(len(line) / 2)
        first = set(line[:length])
        second = set(line[length:])
        same = first & second
        part1 += prio.index(same.pop()) + 1
    
    part2 = 0
    while lines:
        first = set(lines.pop())
        second = set(lines.pop())
        third = set(lines.pop())
        same = first & second & third
        part2 += prio.index(same.pop()) + 1

    return part1, part2

if __name__ == "__main__": 
    input_file = "input.txt"
    #input_file = "test_input.txt"
    with (Path(__file__).parent / input_file).open() as input:
        print(main(input.read()))