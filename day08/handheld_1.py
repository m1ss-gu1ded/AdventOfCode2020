with open("input_08.txt") as file:
    instr_list = file.readlines()

# generating a list of lists, with each item a pair of instruction and amount
instr_list = [(x.strip()) for x in instr_list]
instr_list = [(y.split(" ")) for y in instr_list]

# getting hold of all the executed instruction lines
indices_visited = []


def accumulate(num, accu):
    accu += num
    return accu


def jump_to(index, accu):
    # ends the program if an instruction line is called twice for the first time
    if index in indices_visited:
        print(f"Accumulator is: {accu}")
    else:
        # remember the presently executed instruction line
        indices_visited.append(index)
        instruction = instr_list[index][0]
        amount = int(instr_list[index][1])
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
