with open("input_07.txt") as file:
    rule_list = file.readlines()

# stripping each line of the new line char
rule_list = [(x.strip()) for x in rule_list]
# lose the bag and bags
rule_list = [(x.replace(" bags", "")) for x in rule_list]
rule_list = [(x.replace(" bag", "")) for x in rule_list]

# generating a dictionary for the rules
rule_dict = {}
for rule in rule_list:
    (key, value) = rule.split(" contain ")
    rule_dict[key] = value

# set for  unique bags
colours = set()


# recursive function that searches for occurrences of the colour
def search_colour(colour):
    for colour_key in rule_dict.keys():
        if colour in rule_dict[colour_key]:
            print(f"{colour} in {colour_key}")
            colours.add(colour_key)
            search_colour(colour_key)


search_colour("shiny gold")
# print(colours)
num_of_bag_colours = len(colours)
print(f"Number of bag colours that can contain a shiny golden bag: {num_of_bag_colours}")
