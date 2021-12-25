def ALU(lines, sw, sx, sy, sz):
    v = {"w": sw, "x": sx, "y": sy, "z": sz}
    for op in lines:
        operator = op[0]
        first = op[1]
        if len(op) == 3:
            second = op[2]
            try:
                second = int(second)
            except Exception:
                second = v[second]
        else:
            second = None
        if operator == "inp":
            v[first] = sw
        if operator == "add":
            v[first] += second
        if operator == "mul":
            v[first] *= second
        if operator == "div":
            v[first] = int(v[first] / second)
        if operator == "mod":
            v[first] = v[first] % second
        if operator == "eql":
            v[first] = int(v[first] == second)
    return v["w"], v["x"], v["y"], v["z"]


def solve(parts, lowest=False):
    result = {(0,0,0): ""}
    for i in range(14):
        part = parts[i]
        operations = [["inp", "w"]] + [line.strip().split(" ") for line in part.split("\n")]
        new_result = {}
        for state, values in result.items():
            for u in range(1,10):
                w = 10 - u if lowest else u
                _, x, y, z = ALU(operations, w, *state)
                if i == 13:
                    if z == 0:
                        new_result[(x,y,z)] = values + str(w)
                elif z < 1000000:
                    new_result[(x,y,z)] = values + str(w)
        result = new_result
        #rint(i, len(new_result))
    return int(list(result.values())[0])


def main(input):
    parts = [part.strip() for part in input.read().split("inp w\n")[1:]]

    result1 = solve(parts, lowest=False)
    result2 = solve(parts, lowest=True)

    return result1, result2


TEST_EXPECTED = 96979989692495, 51316214181141
PUZZLE_EXPECTED = 96979989692495, 51316214181141