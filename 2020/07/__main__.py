from pathlib import Path

with (Path(__file__).parent / "input.txt").open() as input:
    rules = {}
    for line in input.read().split(".\n"):
        outer = " ".join(line.split(" ")[:2])
        inner = {" ".join(inner.split(" ")[1:3]): int(inner.split(" ")[0])
                 for inner in line.split("contain ")[1].split(", ")
                 if inner.split(" ")[0] != "no"}
        rules[outer] = inner

    def has_inner_shiny(bag):
        return any(inner_bag == "shiny gold" or has_inner_shiny(inner_bag) for inner_bag in rules[bag].keys())
    part1 = sum(has_inner_shiny(key) for key in rules.keys())
    print("PART 1:", part1)

    def count_bags_in_bag(bag):
        return sum(count * (1 + count_bags_in_bag(inner_bag)) for inner_bag, count in rules[bag].items())
    part2 = count_bags_in_bag("shiny gold")
    print("PART 2:", part2)
    
