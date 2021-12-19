class Node:
    def __init__(self, data):
        if type(data) is list:
            self.left = Node(data[0])
            self.right = Node(data[1])
            self.data = None
        else:
            self.left = None
            self.right = None
            self.data = data

    def explode(self, depth=0):
        if self.data is not None:
            return False, None, None
        elif depth == 4:
            left, right = self.left.data, self.right.data
            self.left = None
            self.right = None
            self.data = 0
            return True, left, right
        else:
            exploded, left, right = self.left.explode(depth + 1)
            if exploded:
                if right:
                    self.right.add_to_first(right)
                return exploded, left, None
            exploded, left, right = self.right.explode(depth + 1)
            if exploded:
                if left:
                    self.left.add_to_last(left)
                return exploded, None, right
            return False, None, None

    def split(self):
        if self.data is not None:
            if self.data >= 10:
                self.left = Node(int(self.data / 2))
                self.right = Node(self.data - int(self.data / 2))
                self.data = None
                return True
        else:
            return self.left.split() or self.right.split()

    def _reduce(self):
        while True:
            #print(self)
            result, *_  = self.explode()
            if result:
                continue
            if self.split():
                continue
            else:
                break

    def add_to_last(self, new):
        if self.data is not None:
            self.data += new
        else:
            self.right.add_to_last(new)

    def add_to_first(self, new):
        if self.data is not None:
            self.data += new
        else:
            self.left.add_to_first(new)

    def magnitude(self):
        if self.data is not None:
            return self.data
        else:
            return 3 * self.left.magnitude() + 2 * self.right.magnitude()

    def add(self, new):
        new_node = Node(None)
        new_node.left = self
        new_node.right = new
        new_node._reduce()
        return new_node

    def copy(self):
        return Node(eval(str(self)))

    def __repr__(self):
        if self.data is not None:
            return str(self.data)
        else:
            return f"[{self.left},{self.right}]"



def main(input):
    nodes = [Node(eval(line.strip())) for line in input.readlines()]
    total = nodes[0].copy()
    for node in nodes[1:]:
        total = total.add(node.copy())

    result1 = total.magnitude()

    result2 = 0
    for i, first in enumerate(nodes):
        for j, second in enumerate(nodes):
            if i == j:
                continue
            magnitude = first.copy().add(second.copy()).magnitude()
            if magnitude > result2:
                result2 = magnitude

    return result1, result2


TEST_EXPECTED = None, None
PUZZLE_EXPECTED = None, None