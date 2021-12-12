from collections import defaultdict

def main(input):
    connections = defaultdict(list)
    for line in input.readlines():
        pair = line.strip().split("-")
        connections[pair[0]].append(pair[1])
        connections[pair[1]].append(pair[0])

    result1, result2 = 0, 0
    path, options = ["start"], connections["start"]
    small_twice = None

    while options:
        option = options.pop()

        if path and option == path[-1]:
            path.pop()
            small_twice = None if small_twice == option else small_twice
            continue
        if option == "start":
            continue
        if option == "end":
            result1 += 0 if small_twice else 1
            result2 += 1
            continue
        if option.islower() and option in path and small_twice:
            continue
        if option.islower() and option in path:
            small_twice = option

        path.append(option)
        options.append(option)
        options += connections[option]

    return result1, result2


TEST_EXPECTED = 10, 36
PUZZLE_EXPECTED = 3779, 96988