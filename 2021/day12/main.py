from collections import defaultdict

def main(input):
    connections = defaultdict(list)
    for line in input.readlines():
        pair = line.strip().split("-")
        connections[pair[0]].append(pair[1])
        connections[pair[1]].append(pair[0])

    result1, result2 = 0, 0
    solver = [(["start"], connections["start"])]
    small_twice = None

    while solver:
        path, options = solver[-1]
        if not options:
            solver.pop()
            small_twice = None if small_twice == path.pop() else small_twice
            continue

        option = options.pop()
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
        solver.append((path + [option], connections[option].copy()))

    return result1, result2


TEST_EXPECTED = 10, 36
PUZZLE_EXPECTED = 3779, 96988