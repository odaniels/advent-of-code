from pathlib import Path
from collections import deque 
from itertools import islice

cups = deque([int(cup) for cup in "135468729"] + list(range(10, 1000001)))
inserted = {}

def insert_values():
    while True:
        for i, value in enumerate(islice(cups, 0, 4)):
            if value in inserted.keys():
                new_val = inserted[value].popleft()
                cups.insert(i + 1, new_val)
                if inserted[value]:
                    while new_val in inserted:
                        new_val = inserted[new_val][-1]
                    else:
                        inserted[new_val] = inserted[value]
                        del inserted[value]
                else:
                    del inserted[value]
                break
        else:
            break

for move in range(10000000):
    if not move % 10000: 
        print(move)
    insert_values()
    current = cups.popleft()
    cups.append(current)
    picked = [cups.popleft() for _ in range(3)]
    destination = next((current - 2 - i) % 1000000 + 1 for i in range(4)
                       if (current - 2 - i) % 1000000 + 1 not in picked)
    if destination in inserted:
        inserted[destination].appendleft(picked[2])
        inserted[destination].appendleft(picked[1])
        inserted[destination].appendleft(picked[0])
    else:
        inserted[destination] = deque(picked)

while cups[0] != 1:
    insert_values()
    current = cups.popleft()

print("PART 2:", cups[1] * cups[2])
