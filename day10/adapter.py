with open("input_10.txt") as file:
    adapter_list = file.readlines()
adapter_list = [x.strip() for x in adapter_list]
adapter_list = [int(x) for x in adapter_list]

# adding the joltage of the output
adapter_list.append(0)
adapter_list.sort()

# print(adapter_list)

difference_list = []

for i in range(1, len(adapter_list)):
    difference = adapter_list[i] - adapter_list[i-1]
    difference_list.append(difference)

# adding the difference of the devices built-in adapter
difference_list.append(3)

cnt_of_1_jlt_diff = difference_list.count(1)
cnt_of_3_jlt_diff = difference_list.count(3)
print(f"There are {cnt_of_1_jlt_diff} differences of 1 jolt.")
print(f"There are {cnt_of_3_jlt_diff} differences of 3 jolts.")

solution = cnt_of_1_jlt_diff * cnt_of_3_jlt_diff
print(f"Solution for part 1: {solution}")

# Part 2

# only a sequence of 1 jolt differences can be replaced by other adapters...
sequence = []
# so isolating the sequences in a list of lists...
sequence_list = []
for diff_item in difference_list:
    if diff_item == 1:
        sequence.append(diff_item)
    else:
        if sequence:
            sequence_list.append(sequence)
            sequence = []
print(sequence_list)

# ... and counting the amount of ones.
count_list = []
for seq_item in sequence_list:
    count_list.append(seq_item.count(1))
print(count_list)

# Figured out the relationship of amount of ones to distinct arrangements with pen and paper...
distinct_ways = 1
for item in count_list:
    if item == 2:
        distinct_ways *= 2
    elif item == 3:
        distinct_ways *= 4
    elif item == 4:
        distinct_ways *= 7
print(f"Total number of distinct ways: {distinct_ways}")
