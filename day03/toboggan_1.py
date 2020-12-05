with open("input_03.txt") as file:
    area = file.readlines()
area = [(x.strip()) for x in area]

# using variables, because I'll probably need those in the 2nd half
right = 3
down = 1
index_right = right
index_down = down

max_y = len(area) - 1
line_length = len(area[0])
max_x = line_length - 1
num_of_trees = 0

for y in range(max_y):

    # taking care of the pattern repetition
    if index_right > max_x:
        index_right -= line_length

    # checking for a tree
    if area[index_down][index_right] == "#":
        num_of_trees += 1

    # move further
    index_right += right
    index_down += down

print(f"Trees encountered: {num_of_trees}")
