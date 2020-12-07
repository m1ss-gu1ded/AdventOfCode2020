with open("input_07.txt") as file:
    rule_list = file.readlines()

# stripping each line of the new line char
rule_list = [(x.strip()) for x in rule_list]
# lose the bag and bags
rule_list = [(x.replace(" bags", "")) for x in rule_list]
rule_list = [(x.replace(" bag", "")) for x in rule_list]
rule_list = [(x.replace(".", "")) for x in rule_list]

# generating a dictionary for the rules
rule_dict = {}
for rule in rule_list:
    (key, value) = rule.split(" contain ")
    rule_dict[key] = value

# separating the colours (dic is now a dict of lists)
for key in rule_dict.keys():
    rule_dict[key] = rule_dict[key].split(", ")


def item_interpreter(item):
    bags_per_item = int(item[0])
    bag_colour = ""
    for letter_index in range(2, len(item)):
        bag_colour += item[letter_index]
    return bags_per_item, bag_colour


# recursive function that counts bags per colour
def count_bags(colour, num):
    bag_count = 0
    for item in rule_dict[colour]:
        if item == "no other":
            return 0
        else:
            bags_per_item, bag_colour = item_interpreter(item)
            bag_count += bags_per_item + bags_per_item * count_bags(bag_colour, bag_count)
    return bag_count


print(f'Number of bags a shiny golden bag must contain: {count_bags("shiny gold", 0)}')
