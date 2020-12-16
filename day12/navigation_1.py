with open("input_12.txt") as file:
    instr_list = file.readlines()
instr_list = [x.strip() for x in instr_list]


def check_instr(position, orientation, action, value):
    if action == "N":
        move_wp_north(position, value)
    elif action == "S":
        move_wp_south(position, value)
    elif action == "E":
        move_wp_east(position, value)
    elif action == "W":
        move_wp_west(position, value)
    elif action == "L":
        turn_wp_left(orientation, value)
    elif action == "R":
        turn_wp_right(orientation, value)
    elif action == "F":
        move_forward(position, orientation, value)


def move_wp_north(position, value):
    position[1] += value


def move_wp_south(position, value):
    position[1] -= value


def move_wp_east(position, value):
    position[0] += value


def move_wp_west(position, value):
    position[0] -= value


def turn_wp_left(orientation, value):
    if value == 90:
        orientation[0] -= 1
    elif value == 180:
        orientation[0] -= 2
    elif value == 270:
        orientation[0] -= 3
    if orientation[0] < 1:
        orientation[0] += 4


def turn_wp_right(orientation, value):
    if value == 90:
        orientation[0] += 1
    elif value == 180:
        orientation[0] += 2
    elif value == 270:
        orientation[0] += 3
    if orientation[0] > 4:
        orientation[0] -= 4


def move_forward(position, orientation, value):
    if orientation[0] == 1:
        move_wp_east(position, value)
    elif orientation[0] == 2:
        move_wp_south(position, value)
    elif orientation[0] == 3:
        move_wp_west(position, value)
    elif orientation[0] == 4:
        move_wp_north(position, value)


# pos[0] is east, pos[1] is north
pos = [0, 0]
ori = [1]

for line in instr_list:
    act = line[0]
    val = int(line[1:])

    check_instr(position=pos, orientation=ori, action=act, value=val)
    print(pos)

manhattan = abs(pos[0]) + abs(pos[1])

print(f"Manhattan distance between start and end: {manhattan}")
