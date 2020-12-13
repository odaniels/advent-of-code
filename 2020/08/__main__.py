from pathlib import Path

with (Path(__file__).parent / "input.txt").open() as input:
    lines = input.read().split("\n")
    for switch_index, switch_instr in enumerate(lines):
        lines[switch_index] = lines[switch_index].replace("jmp", "nop")
        calls = [0] * len(lines)
        acc = 0
        index = 0
        while index < len(lines):
            if calls[index]:
                print("PART 1:", acc)
                break
            else:
                calls[index] += 1
            
            instr, value = lines[index].split(" ")
            if instr == "nop":
                pass
            if instr == "acc":
                acc += int(value)
            if instr == "jmp":
                index += int(value)
            else:
                index += 1
        else:
            print("PART 2:", acc)
            exit()
        
        lines[switch_index] = switch_instr