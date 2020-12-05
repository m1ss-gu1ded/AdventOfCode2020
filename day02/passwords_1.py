with open("input_02.txt") as report:
    pw_list = report.readlines()
pw_list = [(x.strip()) for x in pw_list]
pw_list = [(y.split(": ")) for y in pw_list]

num_of_valid_pw = 0

for item in pw_list:
    rule = item[0].split()
    pw = item[1]
    amount = rule[0].split()
    letter = rule[1]
    nums = amount[0].split("-")
    mini = int(nums[0])
    maxi = int(nums[1])
    num_of_occ = pw.count(letter)

    if mini <= num_of_occ <= maxi:
        num_of_valid_pw += 1

print(f"Number of valid passwords: {num_of_valid_pw}")
