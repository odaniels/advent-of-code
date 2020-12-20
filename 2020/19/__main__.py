from pathlib import Path

rules = {}

def is_valid(rule, input):
    # print(rule, input)
    val = 0
    if '"' in rule:
        val = 1 if rule[1] == input[0] else 0
    elif rule == "42 | 42 8": # -> 42 | 42 42 | 42 42 42
        matches = 0
        while True:
            if not input[matches:]:
                val = matches
                break
            new_matches = is_valid("42", input[matches:])
            if (new_matches):
                matches += new_matches
            else:
                val = matches
                break
        group_matches = int(matches / 8)
        val = [m * 8 + 8 for m in range(group_matches)] 
    elif rule == "42 31 | 42 11 31": # -> 42 31 | 42 42 31 31 | 42 42 42 31 31 31
        for i in range(int(len(input) / 10)):
            test_rule = " ".join(["42"] * (i+1) + ["31"] * (i+1))
            matches = is_valid(test_rule, input)
            if (matches):
                val = matches
                break
        else:
            val = 0
    elif "|" in rule:
        first, second = rule.split("|")
        val = is_valid(first.strip(), input) or is_valid(second.strip(), input)
    else:
        first = rule.split(" ")[0]
        second = " ".join(rule.split(" ")[1:])
        first_matches = is_valid(rules[int(first)], input)
        if first_matches:
            if not isinstance(first_matches, list):
                first_matches = [first_matches]
            if second:
                val = []
                for first_match in first_matches:
                    if first_match == len(input):
                        continue
                    second_matches = is_valid(second, input[first_match:])
                    if second_matches:
                        val.append(first_match + second_matches)
            else:
                val = first_matches
            if not val:
                val = 0
            elif len(val) == 1:
                val = val[0]
        else:
            val = 0
    return val
    
        

curr_dir = Path(__file__).parent
with (curr_dir / "input.txt").open() as input:
    raw_rules, data = input.read().split("\n\n")
    rules = {int(rule.split(":")[0]): rule.split(":")[1].strip() for rule in raw_rules.split("\n")}
    print("PART 1:", sum(len(line) == is_valid(rules[0], line) for line in data.split("\n")))
    rules[8] = "42 | 42 8" # -> 42 | 42 42 | 42 42 42
    rules[11] = "42 31 | 42 11 31" # -> 42 31 | 42 42 31 31 | 42 42 42 31 31 31
    part2 = 0
    for line in data.split("\n"):
        res = is_valid(rules[0], line)
        res = [res] if isinstance(res, int) else res
        part2 += 1 if len(line) in res else 0
    print("PART 2:", part2)