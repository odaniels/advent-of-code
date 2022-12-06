from pathlib import Path

def main(line):
    for part1, _ in enumerate(line):
        message = line[part1-4:part1]
        if part1 >= 4 and len(set(message)) == len(message):
            break
    for part2, _ in enumerate(line):
        message = line[part2-14:part2]
        if part2 >= 14 and len(set(message)) == len(message):
            break
    return part1, part2

if __name__ == "__main__": 
    input_file = "input.txt"
    #input_file = "test_input.txt"
    with (Path(__file__).parent / input_file).open() as input:
        print(main(input.read()))