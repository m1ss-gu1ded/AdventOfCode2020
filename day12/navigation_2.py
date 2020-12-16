with open("input_12.txt") as file:
    instr_list = file.readlines()
instr_list = [x.strip() for x in instr_list]


def check_instr(waypoint, position, action, value):
    if action == "N":
        move_north(waypoint, value)
    elif action == "S":
        move_south(waypoint, value)
    elif action == "E":
        move_east(waypoint, value)
    elif action == "W":
        move_west(waypoint, value)
    elif action == "L":
        turn_left(waypoint, value)
    elif action == "R":
        turn_right(waypoint, value)
    elif action == "F":
        move_forward(waypoint, position, value)


def move_north(waypoint, value):
    waypoint[1] += value


def move_south(waypoint, value):
    waypoint[1] -= value


def move_east(waypoint, value):
    waypoint[0] += value


def move_west(waypoint, value):
    waypoint[0] -= value


def turn_left(waypoint, value):
    east = waypoint[0]
    north = waypoint[1]
    if value == 90:
        waypoint[0] = -north
        waypoint[1] = east
    elif value == 180:
        waypoint[0] = -east
        waypoint[1] = -north
    elif value == 270:
        waypoint[0] = north
        waypoint[1] = -east


def turn_right(waypoint, value):
    if value == 90:
        value += 180
        turn_left(waypoint, value)
    elif value == 180:
        turn_left(waypoint, value)
    elif value == 270:
        value -= 180
        turn_left(waypoint, value)


def move_forward(waypoint, position, value):
    for x in range(0, value):
        position[0] += waypoint[0]
        position[1] += waypoint[1]


# wp/pos: [0] is east, [1] is north
wp = [10, 1]
pos = [0, 0]
ori = [1]


for line in instr_list:
    act = line[0]
    val = int(line[1:])

    check_instr(waypoint=wp, position=pos, action=act, value=val)
    print(pos)
    print(wp)

manhattan = abs(pos[0]) + abs(pos[1])

print(f"Manhattan distance between start and end: {manhattan}")
