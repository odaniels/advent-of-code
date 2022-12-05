from pathlib import Path
from collections import defaultdict

def main(input):
    lines, instructions = input.split("\n\n")
    lines = lines.split("\n")

    crates_str = defaultdict(lambda: "")
    number_of_crates = (len(lines[-1])+1)//4
    for line in reversed(lines[:-1]):
        for i in range(number_of_crates):
            crates_str[i+1] += line[1+4*i]
    
    crates = {key: list(string.strip()) for key, string in crates_str.items()}
    crates2 = {key: list(string.strip()) for key, string in crates_str.items()}

    for line in instructions.split("\n"):
        parts = line.split(" ")
        num = int(parts[1])
        src = int(parts[3])
        dst = int(parts[5])
        
        # part1
        for _ in range(num):
            crates[dst].append(crates[src].pop())
        
        # part2
        move2 = crates2[src][-num:]
        crates2[src] = crates2[src][:-num]
        crates2[dst] += move2

    return (
        "".join(crate[-1] for crate in crates.values()),
        "".join(crate[-1] for crate in crates2.values())
    )

if __name__ == "__main__": 
    input_file = "input.txt"
    #input_file = "test_input.txt"
    with (Path(__file__).parent / input_file).open() as input:
        print(main(input.read()))