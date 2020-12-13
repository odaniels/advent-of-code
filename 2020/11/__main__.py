from pathlib import Path
import itertools

DIRECTIONS = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 0), (0, 1), (-1, -1), (-1, 0), (-1, 1)]


curr_dir = Path(__file__).parent
with (curr_dir / "input.txt").open() as input:
    seats = input.read().split("\n")
    max_rows = len(seats)
    max_cols = len(seats[0])
    prev_occupied_seats = 1000
    iterations = 0
    
    def has_any_neighbor(seats, row, col):
        return any(seats[row + r][col + c] == "#" for r, c in DIRECTIONS
                   if 0 <= row + r < max_rows and 0 <= col + c < max_cols)

    def has_too_many_neighbor(seats, row, col):
        return sum(seats[row + r][col + c] == "#" for r, c in DIRECTIONS
                   if 0 <= row + r < max_rows and 0 <= col + c < max_cols) > 4

    def see_any_neighbor(seats, row, col):
        for r, c in DIRECTIONS:
            i = 1
            while 0 <= row + r * i < max_rows and 0 <= col + c * i < max_cols:
                if seats[row + r * i][col + c * i] == "#":
                    return True
                elif seats[row + r * i][col + c * i] == "L":
                    break
                i += 1
    
    def see_too_many_neighbor(seats, row, col):
        number_of_neighbors = 0
        for r, c in DIRECTIONS:
            i = 1
            while 0 <= row + r * i < max_rows and 0 <= col + c * i < max_cols:
                if seats[row + r * i][col + c * i] == "#":
                    number_of_neighbors += 1
                    if number_of_neighbors > 5:
                        return True
                    else:
                        break
                elif seats[row + r * i][col + c * i] == "L":
                    break
                i += 1

    while iterations < 1000:
        new_seats = []
        iterations += 1
        total_occupied_seats = sum(sum(seat == "#" for seat in row) for row in seats)
        if prev_occupied_seats == total_occupied_seats:
            print("PART 2:", total_occupied_seats)
            break
        else:
            print(abs(prev_occupied_seats - total_occupied_seats))
            prev_occupied_seats = total_occupied_seats
        for row, seats_in_row in enumerate(seats):
            new_row = ""
            for col, seat in enumerate(seats_in_row):
                if seat == ".":
                    new_row += "."
                    continue
                elif seat == "L":
                    new_row += "#" if not see_any_neighbor(seats, row, col) else "L"
                elif seat == "#":
                    new_row += "L" if see_too_many_neighbor(seats, row, col) else "#"
            new_seats.append(new_row)
        seats = new_seats.copy()
        new_seats = []
