def transform(subject_number, loop_size):
    value = 1
    for _ in range(loop_size):
        value = (value * subject_number) % 20201227
    return value


def find_loop_size(subject_number, public_key):
    value = 1
    loop_size = 0
    while value != public_key:
        loop_size += 1
        value = (value * subject_number) % 20201227
    else:
        return loop_size


card_public_key = 19774466
door_public_key = 7290641
door_loop_size = find_loop_size(7, door_public_key)
encryption_key = transform(card_public_key, door_loop_size)
print("PART1:", encryption_key)
