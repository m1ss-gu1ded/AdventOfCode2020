with open("input_16.txt") as file:
    data = file.readlines()

data = [x.strip() for x in data]
# remove empty strings
data = list(filter(None, data))

# extract rule values
slice_index = data.index("your ticket:")
ranges = data[slice(slice_index)]
range_list = []
for item in ranges:
    range_items = item[item.index(":") + 2:].split(" or ")
    range_list.append(range_items)
pair_list = []
for item in range_list:
    item = [x.split("-") for x in item]
    pair_list.append(item)

# extract ticket values
slice_index = data.index("nearby tickets:")
tickets = data[slice(slice_index + 1, len(data))]
ticket_list = [x.split(",") for x in tickets]

# check tickets against rules
error_rate = 0
for ticket in ticket_list:
    for num in ticket:
        check_list = []
        num = int(num)
        for item in pair_list:
            pi = pair_list.index(item)
            min1 = int(pair_list[pi][0][0])
            max1 = int(pair_list[pi][0][1])
            min2 = int(pair_list[pi][1][0])
            max2 = int(pair_list[pi][1][1])
            if min1 <= num <= max1 or min2 <= num <= max2:
                check_list.append(True)
        if True not in check_list:
            print(f"invalid number: {num}")
            error_rate += num
print(f"Error rate: {error_rate}")

