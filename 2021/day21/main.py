from functools import lru_cache


def part1(pos1, pos2):
    turn, dice, score1, score2 = 0, 0, 0, 0
    while True:
        dice_value = (1 + (dice % 100))
        dice += 1
        if turn < 3:
            pos1 = 1 + ((pos1 - 1 + dice_value) % 10)
        if turn == 2:
            score1 += pos1
            if score1 >= 1000:
                return score2 * dice
        if turn > 2:
            pos2 = 1 + ((pos2 - 1 + dice_value) % 10)
        if turn == 5:
            score2 += pos2
            if score2 >= 1000:
                return score1 * dice
        turn = (turn + 1) % 6


@lru_cache(None)
def part2(pos1, pos2, turn, score1, score2):
    wins1, wins2 = 0, 0
    for i in range(3):
        dice_value = i + 1
        new_score1 = score1
        new_score2 = score2
        if turn < 3:
            new_pos1 = 1 + ((pos1 - 1 + dice_value) % 10)
            new_pos2 = pos2
            if turn == 2:
                new_score1 = score1 + new_pos1
                if new_score1 >= 21:
                    wins1 += 1
                    continue
        if turn > 2:
            new_pos2 = 1 + ((pos2 - 1 + dice_value) % 10)
            new_pos1 = pos1
            if turn == 5:
                new_score2 = score2 + new_pos2
                if new_score2 >= 21:
                    wins2 += 1
                    continue
        _wins1, _wins2 = part2(new_pos1, new_pos2, (turn + 1) % 6, new_score1, new_score2)
        wins1 += _wins1
        wins2 += _wins2
    return wins1, wins2


def main(input):
    pos1, pos2 = map(int, input.read().strip().split(","))

    result1 = part1(pos1, pos2)
    result2 = max(part2(pos1, pos2, 0, 0, 0))
    return result1, result2


TEST_EXPECTED = 739785, 444356092776315
PUZZLE_EXPECTED = 900099, 306719685234774