with open("input_03.txt") as file:
    area = file.readlines()
area = [(x.strip()) for x in area]


def number_of_trees(right, down):
    index_right = right
    index_down = down

    max_y = len(area) - 1
    line_length = len(area[0])
    max_x = line_length - 1
    num_of_trees = 0

    # step added for slopes with down > 1
    for y in range(0, max_y, down):

        # taking care of the pattern repetition
        if index_right > max_x:
            index_right -= line_length

        # checking for a tree
        if area[index_down][index_right] == "#":
            num_of_trees += 1

        # move further
        index_right += right
        index_down += down

    print(f"Trees encountered with {right} right and {down} down: {num_of_trees}")

    return num_of_trees


slope1 = number_of_trees(1, 1)
slope2 = number_of_trees(3, 1)
slope3 = number_of_trees(5, 1)
slope4 = number_of_trees(7, 1)
slope5 = number_of_trees(1, 2)

solution = slope1 * slope2 * slope3 * slope4 * slope5
print(f"Solution: {solution}")
