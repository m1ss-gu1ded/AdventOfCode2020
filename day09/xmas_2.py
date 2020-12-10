with open("input_09.txt") as file:
    num_list = file.readlines()

num_list = [(x.strip()) for x in num_list]

len_list = len(num_list)
invalid_num = 105950735

for i in range(len_list):
    num = int(num_list[i])
    num_sum = 0
    num_set = []
    for j in range(i + 1, len_list):
        next_num = int(num_list[j])
        num_set.append(next_num)
        num_sum += next_num
        if len(num_set) > 1 and num_sum == invalid_num:
            print(f"{num_set} is the range adding up to {invalid_num}")
            num_set.sort()
            solution = num_set[0] + num_set[-1]
            print(f"solution: {solution}")
        elif num_sum > invalid_num:
            break
