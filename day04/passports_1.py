file = open("input_04.txt")

# read file as a whole
id_list = file.read()

# split into list of single ids
id_list = id_list.split("\n\n")

field_list = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
num_of_valid_ids = 0

for item in id_list:
    # count only ids with all fields
    if all(field in item for field in field_list):
        num_of_valid_ids += 1

print(f"Number of valid passports: {num_of_valid_ids}")
