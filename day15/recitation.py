with open("input_15.txt") as file:
    numbers = file.read()
numbers = numbers.split(",")
initial_len = len(numbers)


def recite(max_count):
    num_dict = {}
    for num in numbers:
        num_dict.update({int(num): numbers.index(num) + 1})

    count = initial_len
    last_num = max(num_dict, key=num_dict.get)

    while count < max_count:
        if last_num in num_dict:
            new_num = last_num
            last_num = count - num_dict[last_num]
            num_dict[new_num] = count
        else:
            num_dict[last_num] = count
            last_num = 0
        count += 1
        # print(last_num)
    print(f"final number in round {max_count}: {last_num}")


recite(2020)
recite(30000000)
