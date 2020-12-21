from pathlib import Path

curr_dir = Path(__file__).parent
with (curr_dir / "input.txt").open() as input:
    rows = input.read().split("\n")

    allergens_dict = {}
    all_ingredients = set()
    for row in rows:
        first, second = row.split(" (contains ")

        ingredients = set(first.split())
        all_ingredients |= ingredients

        allergenes = second[:-1].split(", ")
        for allergen in allergenes:
            if allergen in allergens_dict:
                allergens_dict[allergen] &= ingredients
            else:
                allergens_dict[allergen] = ingredients.copy()

    free_ingredients = all_ingredients.copy()
    for ingredients in allergens_dict.values():
        free_ingredients -= ingredients
    print("PART 1:", sum(sum(ingredient in row.split() for row in rows) for ingredient in free_ingredients))

    while not all(len(n) == 1 for n in allergens_dict.values()):
        for key, value in allergens_dict.items():
            if len(value) == 1:
                for other_key in allergens_dict.keys():
                    if key != other_key:
                        allergens_dict[other_key] -= value
    print("PART 2:", ",".join([next(iter(allergens_dict[key])) for key in sorted(allergens_dict)]))