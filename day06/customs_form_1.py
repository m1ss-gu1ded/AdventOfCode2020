file = open("input_06.txt")

# read file as a whole
answer_list = file.read()
file.close()

# split into list of group answers
answer_list = answer_list.split("\n\n")
num_sum = 0

for group in answer_list:

    # removing new lines
    group = group.replace("\n", " ")

    # finding the unique letters through a set
    unique_letters = set(group)
    unique_letters.discard(" ")
    num_of_answers = len(unique_letters)

    num_sum += num_of_answers

print(f"Sum of questions answered with 'Yes': {num_sum}")
