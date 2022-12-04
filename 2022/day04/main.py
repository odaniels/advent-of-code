from pathlib import Path

def main(input):
    lines = [in_line.split(",") for in_line in input.split("\n")]
    part1, part2 = 0,0
    for first, second in lines:
        f1, f2 = map(int, first.split("-"))
        first_range = set(range(f1,f2+1))
        s1, s2 = map(int, second.split("-"))
        second_range = set(range(s1,s2+1))
        overlap = first_range & second_range
        if len(overlap) in [len(first_range), len(second_range)]:
            part1 += 1
        if len(overlap):
            part2 += 1

    return part1, part2

if __name__ == "__main__": 
    input_file = "input.txt"
    #input_file = "test_input.txt"
    with (Path(__file__).parent / input_file).open() as input:
        print(main(input.read()))