with open("input_05.txt") as file:
    bp_list = file.readlines()

# stripping each line of the new line char
bp_list = [(x.strip()) for x in bp_list]

# setting the min and max values in case I need to change them in pt.2
lower = 0
upper = 127
left = 0
right = 7
id_list = []

for item in bp_list:
    # resetting the values for each boarding pass
    upper_row = upper
    lower_row = lower
    num_of_rows = upper + 1
    upper_seat = right
    lower_seat = left
    num_of_seats = right + 1

    # traversing each character
    for char in item:

        # when row is set, determining the seat
        if upper_row == lower_row:
            # binary partitioning ftw
            num_of_seats = int(num_of_seats / 2)
            # deciding if lower or upper half
            if char == "L":
                upper_seat -= num_of_seats
            else:
                lower_seat += num_of_seats

        else:
            # determining the row
            num_of_rows = int(num_of_rows / 2)
            if char == "F":
                upper_row -= num_of_rows
            else:
                lower_row += num_of_rows

    seat_id = lower_row * 8 + lower_seat
    id_list.append(seat_id)

id_list.sort(reverse=True)
print(id_list)
highest_id = id_list[0]
print(f"Highest seat ID: {highest_id}")


# Part 2
id_list.sort()
counter = id_list[0]

# find the gap through comparison with a counter
for item in id_list:
    if counter != item:
        break
    counter += 1

print(f"The missing seat is: {counter}")
