from pathlib import Path
from copy import deepcopy


def calc_scores(decks):
    return {player: sum(card * (len(cards) - i) for i, card in enumerate(cards))
            for player, cards in decks.items()}


def run_regular_combat(decks):
    while all(sum(cards) for cards in decks.values()):
        p1 = decks["Player 1"].pop(0)
        p2 = decks["Player 2"].pop(0)
        if p1 > p2:
            decks["Player 1"] += [p1, p2]
        else:
            decks["Player 2"] += [p2, p1]
    else:
        return decks


def run_recursive_combat(decks):
    played_decks = {player: set() for player, _ in decks.items()}

    while all(sum(cards) for cards in decks.values()):
        if any(tuple(c) in played_decks[p] for p, c in decks.items()):
            decks["Player 2"] = []
            break
        else:
            played_decks["Player 1"].add(tuple(decks["Player 1"]))
            played_decks["Player 2"].add(tuple(decks["Player 2"]))

        p1 = decks["Player 1"].pop(0)
        p2 = decks["Player 2"].pop(0)

        if len(decks["Player 1"]) >= p1 and len(decks["Player 2"]) >= p2:
            recursive_decks = run_recursive_combat(
                {
                    "Player 1": decks["Player 1"].copy()[:p1], 
                    "Player 2": decks["Player 2"].copy()[:p2]
                }
            )
            p1_won = "Player 1" in (player for player, cards in recursive_decks.items() if cards)
        else:
            p1_won = p1 > p2
        
        if p1_won:
            decks["Player 1"] += [p1, p2]
        else:
            decks["Player 2"] += [p2, p1]

    return decks

curr_dir = Path(__file__).parent
with (curr_dir / "input.txt").open() as input:
    start_deck = {deck_input.split("\n")[0][:-1]:
                  [int(card) for card in deck_input.split("\n")[1:]]
                  for deck_input in input.read().split("\n\n")}
    
    regular_combat = run_regular_combat(deepcopy(start_deck))
    print("PART 1:", calc_scores(regular_combat))

    recursive_combat = run_recursive_combat(deepcopy(start_deck))
    print("PART 2:", calc_scores(recursive_combat))
