from pathlib import Path


input_file = "input.txt"
#input_file = "test_input.txt"
with (Path(__file__).parent / input_file).open() as input_file:
    lines = [line for line in input_file.read().split("\n\n")]

class Package:
    def __init__(self, package):
        self.package = package

    def __lt__(self, other):
        for i in range(min(len(self.package), len(other.package))):
            f = self.package[i]
            s = other.package[i]
            if isinstance(f, int) and isinstance(s, int):
                if f != s:
                    return f < s
            else:
                ff = [f] if isinstance(f, int) else f
                ss = [s] if isinstance(s, int) else s
                res = Package(ff) < Package(ss)
                if res != None:
                    return res
        if len(self.package) < len(other.package):
            return True
        if len(other.package) < len(self.package):
            return False


part1 = 0
packages = []
for i, line in enumerate(lines, start=1):
    first, second = [Package(eval(part)) for part in line.split("\n")]
    packages += [first, second]
    if first < second:
        part1 += i
print(part1)

divider1 = Package([[2]])
divider2 = Package([[6]])
packages += [divider1, divider2]
packages.sort()
print((packages.index(divider1) + 1) * (packages.index(divider2) + 1))
