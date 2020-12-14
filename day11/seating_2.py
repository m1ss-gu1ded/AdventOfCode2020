# Beware, this takes a while to run!
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
        for i in range(1, max_line - 1):
            if (l + i) > max_line or (r + i) > max_row:
                break
            else:
                if layout[l + i][r + i] != ".":
                    neighbours.append(layout[l + i][r + i])
                    break
    if l > 0 and r > 0:
        for i in range(1, max_line - 1):
            if (l - i) < 0 or (r - i) < 0:
                break
            else:
                if layout[l - i][r - i] != ".":
                    neighbours.append(layout[l - i][r - i])
                    break
    if l > 0:
        for i in range(1, max_line - 1):
            if (l - i) < 0:
                break
            else:
                if layout[l - i][r] != ".":
                    neighbours.append(layout[l - i][r])
                    break
    if l > 0 and r < max_row:
        for i in range(1, max_line - 1):
            if (l - i) < 0 or (r + i) > max_row:
                break
            else:
                if layout[l - i][r + i] != ".":
                    neighbours.append(layout[l - i][r + i])
                    break
    if r > 0:
        for i in range(1, max_line - 1):
            if (r - i) < 0:
                break
            else:
                if layout[l][r - i] != ".":
                    neighbours.append(layout[l][r - i])
                    break
    if r < max_row:
        for i in range(1, max_line - 1):
            if (r + i) > max_row:
                break
            else:
                if layout[l][r + i] != ".":
                    neighbours.append(layout[l][r + i])
                    break
    if l < max_line and r > 0:
        for i in range(1, max_line - 1):
            if (l + i) > max_line or (r - i) < 0:
                break
            else:
                if layout[l + i][r - i] != ".":
                    neighbours.append(layout[l + i][r - i])
                    break
    if l < max_line:
        for i in range(1, max_line - 1):
            if (l + i) > max_line:
                break
            else:
                if layout[l + i][r] != ".":
                    neighbours.append(layout[l + i][r])
                    break

    # Counting the occupied seats
    num_occ = neighbours.count("#")

    if layout[l][r] == "L" and "#" not in neighbours:
        new_seat_layout[l][r] = "#"
    elif layout[l][r] == "#" and num_occ > 4:
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
