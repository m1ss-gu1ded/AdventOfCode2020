with open("input_08.txt") as file:
    instr_list = file.readlines()

# generating a list of lists, with each item a pair of instruction and amount
instr_list = [(x.strip()) for x in instr_list]
instr_list = [(y.split(" ")) for y in instr_list]

# getting hold of all the executed instruction lines
indices_visited = []
accu_list = []


def accumulate(num, accu):
    accu += num
    return accu


def jump_to(index, accu):
    # ends the program if an instruction line is called twice for the first time
    if index not in indices_visited:
        # remember the presently executed instruction line
        indices_visited.append(index)
        accu_list.append(accu)

        # return the Accumulator, when the program tries to step into a non-existent line - aka terminates.
        try:
            instruction = instr_list[index][0]
            amount = int(instr_list[index][1])
        except IndexError:
            print(f"Problem in boot code found! Accumulator after termination is: {accu_list[-1]}")

            # this stops further exceptions
            return None

        if instruction == "acc":
            accu = accumulate(amount, accu)
            jump_to(index + 1, accu)
        elif instruction == "jmp":
            index += amount
            jump_to(index, accu)
        elif instruction == "nop":
            jump_to(index + 1, accu)


# start the program
jump_to(0, 0)

# Part 2

# getting hold of my indices and accumulators to retrace my steps
original_indices_visited = indices_visited
original_accu_list = accu_list

for index in range(len(original_indices_visited) - 1, -1, -1):

    # clear the visited lines list jump_to() uses
    indices_visited = []

    # traversing the (original) visited lines list backwards, change the instruction und see what happens...
    instr_index = original_indices_visited[index]
    instruction = instr_list[instr_index][0]
    accu = original_accu_list[index]
    if instruction == "acc":
        pass
    elif instruction == "jmp":
        instr_list[instr_index][0] = "nop"
        jump_to(instr_index, accu)
        instr_list[instr_index][0] = "jmp"
    elif instruction == "nop":
        instr_list[instr_index][0] = "jmp"
        jump_to(instr_index, accu)
        instr_list[instr_index][0] = "nop"
