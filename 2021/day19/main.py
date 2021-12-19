from collections import deque, Counter

class Scanner:
    def __init__(self, beacons, norms=None, position=None):
        self.position = position or (0,0,0)
        self.beacons = set(beacons)
        self.norms = norms or self.get_norms()

    def copy(self):
        return Scanner(self.beacons.copy(), self.norms.copy(), self.position)

    def rotate_x(self):
        new_beacons = set()
        for beacon in self.beacons:
            new_beacons.add((-beacon[1], beacon[0], beacon[2]))
        self.beacons = new_beacons

    def rotate_y(self):
        new_beacons = set()
        for beacon in self.beacons:
            new_beacons.add((beacon[2], beacon[1], -beacon[0]))
        self.beacons = new_beacons

    def rotate_z(self):
        new_beacons = set()
        for beacon in self.beacons:
            new_beacons.add((beacon[0],-beacon[2], beacon[1]))
        self.beacons = new_beacons

    def translate(self, translation):
        new_beacons = set()
        for beacon in self.beacons:
            new_beacons.add((beacon[0] + translation[0], beacon[1] + translation[1], beacon[2] + translation[2]))
        self.beacons = new_beacons
        self.position = (self.position[0] + translation[0], self.position[1] + translation[1], self.position[2] + translation[2])

    @staticmethod
    def get_beacon_diff(first, other):
        return first[0] - other[0], first[1] - other[1], first[2] - other[2]

    def get_manhattan_diff(self, other):
        pos1 = self.position
        pos2 = other.position
        return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1]) + abs(pos1[2]-pos2[2])

    def get_norms(self):
        beacons = self.beacons.copy()
        norms = []
        while beacons:
            beacon = beacons.pop()
            for other in beacons:
                diff = self.get_beacon_diff(beacon, other)
                norms.append(abs(diff[0]) + abs(diff[1]) + abs(diff[2]))
        print("INIT")
        return norms

    def should_match(self, other):
        c = list((Counter(self.norms) & Counter(other.norms)).elements())
        return len(c) >= 11+10+9+8+7+6+5+4+3+2+1

    def matches(self, other):
        for beacon in self.beacons:
            for other_beacon in other.beacons:
                translation = self.get_beacon_diff(other_beacon, beacon)
                new_scanner = self.copy()
                new_scanner.translate(translation)
                number_of_intersections = len(set(new_scanner.beacons).intersection(other.beacons))
                if number_of_intersections >= 12:
                    self.beacons = new_scanner.beacons.copy()
                    self.position = new_scanner.position
                    return True
        else:
            return False

    def matches_with_rotation(self, other):
        for _ in range(4):
            self.rotate_x()
            for _ in range(4):
                self.rotate_y()
                for _ in range(4):
                    self.rotate_z()
                    if self.matches(other):
                        return True
        else:
            return False

    def print(self):
        print("-----------------")
        for beacon in self.beacons:
            print(beacon)
        print("-----------------")



def main(input):
    scanners = deque(Scanner([tuple(map(int, line.strip().split(","))) for line in lines.split("\n")[1:]])
                for i, lines in enumerate(input.read().split("\n\n")))

    found_scanners = [scanners.popleft()]
    while scanners:
        scanner = scanners.popleft()
        for found_scanner in found_scanners:
            if not scanner.should_match(found_scanner):
                continue
            if scanner.matches_with_rotation(found_scanner):
                found_scanners.append(scanner)
                print(len(scanners))
                break
        else:
            scanners.append(scanner)

    all_beacons = set()
    result2 = 0
    for scanner in found_scanners:
        all_beacons |= scanner.beacons
        for second in found_scanners:
            manhattan = scanner.get_manhattan_diff(second)
            if manhattan > result2:
                result2 = manhattan


    result1 = len(all_beacons)

    return result1, result2


TEST_EXPECTED = None, None
PUZZLE_EXPECTED = None, None