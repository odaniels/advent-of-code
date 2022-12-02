from pathlib import Path

def main(input):
    games = [in_line for in_line in input.split("\n")]
    values = {"X": 1, "Y": 2, "Z": 3}
    results = {
        ("A", "X"): 3,
        ("A", "Y"): 6,
        ("A", "Z"): 0,
        ("B", "X"): 0,
        ("B", "Y"): 3,
        ("B", "Z"): 6,
        ("C", "X"): 6,
        ("C", "Y"): 0,
        ("C", "Z"): 3,
    }
    results2 = {
        ("A", "X"): 0 + values["Z"],
        ("A", "Y"): 3 + values["X"],
        ("A", "Z"): 6 + values["Y"],
        ("B", "X"): 0 + values["X"],
        ("B", "Y"): 3 + values["Y"],
        ("B", "Z"): 6 + values["Z"],
        ("C", "X"): 0 + values["Y"],
        ("C", "Y"): 3 + values["Z"],
        ("C", "Z"): 6 + values["X"],
    }
    score, score2 = 0, 0
    for game in games:
        opp, me = game.split(" ")
        score += values[me] + results[(opp, me)]
        score2 += results2[(opp, me)]
    return score, score2

if __name__ == "__main__": 
    input_file = "input.txt"
    # input_file = "test_input.txt"
    with (Path(__file__).parent / input_file).open() as input:
        print(main(input.read()))