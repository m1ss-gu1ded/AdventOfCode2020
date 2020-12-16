with open("input_14.txt") as file:
    data = file.readlines()
data = [x.strip() for x in data]
data = [x.split(" = ") for x in data]

mem = {}
mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# read line for line
for index in range(len(data)):
    instruction = data[index][0]
    if instruction == "mask":
        mask = data[index][1]
    else:
        # isolate and convert the bit address
        address = instruction.removeprefix("mem[")
        address = int(address.removesuffix("]"))
        address = f"{int(address):036b}"
        address_list = [""]
        # loop over mask
        for i in range(36):
            # 0: leave unchanged
            if mask[i] == "0":
                address_list = [adr + address[i] for adr in address_list]
            # 1: overwrite
            elif mask[i] == "1":
                address_list = [adr + "1" for adr in address_list]
            # floating bit: duplicate list, append 0 to one half, 1 to other half
            else:
                new_address_list = [adr + "0" for adr in address_list]
                address_list = [adr + "1" for adr in address_list]
                address_list += new_address_list
        for item in address_list:
            mem.update({item: data[index][1]})

val_sum = 0
for val in mem.values():
    val_sum += int(val)

print(f"sum of all values: {val_sum}")
