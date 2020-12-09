with open("input_09.txt") as file:
    num_list = file.readlines()

# stripping each line of the new line char
num_list = [(x.strip()) for x in num_list]

len_preamble = 25

for i in range(len_preamble, len(num_list)):
    sum_list = []
    num = int(num_list[i])
    for j in range(i - len_preamble, i):
        for k in range(j + 1, i):
            first_num = int(num_list[j])
            second_num = int(num_list[k])
            num_sum = first_num + second_num
            sum_list.append(num_sum)

    # print(sum_list)

    if num not in sum_list:
        print(f"{num} is not a sum of previous numbers.")
        break
