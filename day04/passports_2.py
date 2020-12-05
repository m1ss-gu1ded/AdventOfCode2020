import re

file = open("input_04.txt")
id_list = file.read()
id_list = id_list.split("\n\n")

field_list = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
colour_list = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
num_of_valid_ids = 0

for single_id in id_list:
    # use only ids with all fields
    if all(field in single_id for field in field_list):
        # removing new lines
        single_id = single_id.replace("\n", " ")

        # generating a dictionary for each id
        id_dict = {}
        pairs = single_id.split()
        for pair in pairs:
            (key, value) = pair.split(":")
            id_dict[key] = value

        # check birth year...
        if 1920 <= int(id_dict["byr"]) <= 2002:
            # issue year...
            if 2010 <= int(id_dict["iyr"]) <= 2020:
                # expiration year...
                if 2020 <= int(id_dict["eyr"]) <= 2030:
                    # hair colour...
                    colour = id_dict["hcl"]
                    match = re.search(r'^#([0-9a-fA-F]{6})$', colour)
                    if match:
                        # eye colour...
                        if id_dict["ecl"] in colour_list:
                            # passport id...
                            pid = id_dict["pid"]
                            match = re.search(r'^[0-9]{9}$', pid)
                            if match:
                                # and height.
                                if "cm" in id_dict["hgt"]:
                                    num = id_dict["hgt"].split("cm", 1)[0]
                                    if 150 <= int(num) <= 193:
                                        num_of_valid_ids += 1
                                elif "in" in id_dict["hgt"]:
                                    num = id_dict["hgt"].split("in", 1)[0]
                                    if 59 <= int(num) <= 76:
                                        num_of_valid_ids += 1

print(f"Number of valid passports: {num_of_valid_ids}")
