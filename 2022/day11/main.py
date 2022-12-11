from pathlib import Path
from collections import deque

input_file = "input.txt"
with (Path(__file__).parent / input_file).open() as input_file:
    monkey_inputs = [in_line for in_line in input_file.read().split("\n\n")]

monkeys = {}
for monkey_lines in monkey_inputs:
    lines = monkey_lines.split("\n")
    monkeys[lines[0][-2]] = {
        "items": deque([int(n.strip()) for n in lines[1].split(":")[1].split(",")]),
        "op": lines[2].split("=")[-1].strip(),
        "division_test": int(lines[3].split(" ")[-1]),
        "if_true": lines[4][-1],
        "if_false": lines[5][-1],
        "inspections": 0
    }

lcm = 1
for monkey in monkeys.values():
    lcm *= monkey["division_test"]

for round in range(10000):
    for number, monkey in monkeys.items():
        while monkey["items"]:
            monkey["inspections"] += 1
            item = monkey["items"].popleft()
            _, operator, x = monkey["op"].split(" ")
            x = item if x == "old" else int(x)
            item = item + x if operator == "+" else item * x
            item = item % lcm
            target = monkey["if_true"] if item % monkey["division_test"] == 0 else monkey["if_false"]
            monkeys[target]["items"].append(item)

a, b = sorted([m["inspections"] for m in monkeys.values()])[-2:]
print(a*b)