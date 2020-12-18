from pathlib import Path
from itertools import groupby


def evaluate2(parts):
    #print(" ".join(parts))
    if len(parts) == 1:
        return int(parts[0])
    elif ")" in parts:
        last_start = 0
        for i, part in enumerate(parts):
            if part == "(":
                last_start = i
            if part == ")":
                new_parts = []
                if last_start != 0:
                    new_parts += parts[:last_start]
                new_parts.append(str(evaluate2(parts[last_start + 1:i])))
                if i + 1 < len(parts):
                    new_parts += parts[i + 1:]
                return evaluate2(new_parts)
    elif "*" in parts and "+" in parts:
        return evaluate2(" * ".join([str(evaluate2(list(group))) 
                                     for p, group in groupby(parts, lambda x: x == "*") 
                                     if not p]).split(" "))
    elif parts[-2] == "+":
        return evaluate2(parts[:-2]) + int(parts[-1])
    else:
        return evaluate2(parts[:-2]) * int(parts[-1])


curr_dir = Path(__file__).parent
with (curr_dir / "input.txt").open() as input:
    part2 = sum(evaluate2(list(line.replace(" ",""))) for line in input.read().split("\n"))
    print("PART 2:", part2)
