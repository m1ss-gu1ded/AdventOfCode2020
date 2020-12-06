# Not an elegant solution and a pain to debug... But it works.

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
    persons_list = group.split()

    num_of_answers = 0

    # checking if it's just one person and all answers are valid
    if len(persons_list) == 1:
        num_of_answers = len(persons_list[0])
    else:
        # sorting the person with the fewest answers in front
        persons_list.sort(key=len)

        # looping through every answer from that person
        for letter in persons_list[0]:
            contains_letter = False
            # comparing it with the next person, and the next...
            for index in range(1, len(persons_list)):
                if letter not in persons_list[index]:
                    contains_letter = False
                    break
                else:
                    contains_letter = True
            if contains_letter:
                num_of_answers += 1

    num_sum += num_of_answers

print(f"Sum of questions answered with 'Yes' by every group member: {num_sum}")
