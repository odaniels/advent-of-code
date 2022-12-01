from pathlib import Path

def main(input):
    elfs = [sum(int(line) for line in in_line.split("\n"))
            for in_line in input.split("\n\n")]
    elfs.sort()
    return max(elfs), sum(elfs[-3:])

if __name__ == "__main__": 
    input_file = "input.txt"
    # input_file = "test_input.txt"
    with (Path(__file__).parent / input_file).open() as input:
        print(main(input.read()))