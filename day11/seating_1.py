import copy

with open("input_11.txt") as file:
    seat_layout = file.readlines()
seat_layout = [list(x.strip()) for x in seat_layout]

max_line = len(seat_layout) - 1
max_row = len(seat_layout[0]) - 1


def check_seats(layout, l, r):

    # Storing the nearest seats in a list, extensive ifs for the edge cases.
    neighbours = []
    if l < max_line and r < max_row:
        neighbours.append(layout[l + 1][r + 1])
    if l > 0 and r > 0:
        neighbours.append(layout[l - 1][r - 1])
    if l > 0:
        neighbours.append(layout[l - 1][r])
    if l > 0 and r < max_row:
        neighbours.append(layout[l - 1][r + 1])
    if r > 0:
        neighbours.append(layout[l][r - 1])
    if r < max_row:
        neighbours.append(layout[l][r + 1])
    if l < max_line and r > 0:
        neighbours.append(layout[l + 1][r - 1])
    if l < max_line:
        neighbours.append(layout[l + 1][r])

    # Counting the occupied seats
    num_occ = neighbours.count("#")

    if layout[l][r] == "L" and "#" not in neighbours:
        new_seat_layout[l][r] = "#"
    elif layout[l][r] == "#" and num_occ >= 4:
        new_seat_layout[l][r] = "L"
    elif layout[l][r] == ".":
        new_seat_layout[l][r] = "."


# Iterating through all the seats
def run_round(s_layout):
    for li in range(len(s_layout)):
        for ri in range(len(s_layout[0])):
            check_seats(s_layout, li, ri)


# Deep copying before each round, otherwise the original list gets written over while iterating through it!
new_seat_layout = copy.deepcopy(seat_layout)
run_round(seat_layout)

# looping until the chaos stabilizes
while seat_layout != new_seat_layout:
    seat_layout = copy.deepcopy(new_seat_layout)
    run_round(seat_layout)

count = 0
for line in seat_layout:
    count += line.count("#")
print(f"Number of occupied seats: {count}")
