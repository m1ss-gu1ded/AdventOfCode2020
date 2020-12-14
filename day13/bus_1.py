with open("input_13.txt") as file:
    timetable = file.readlines()
timetable = [x.strip() for x in timetable]

timestamp = int(timetable[0])
bus_list = timetable[1].split(",")
departure_dict = dict()

for bus in bus_list:
    if bus == "x":
        pass
    else:
        bus = int(bus)
        departure = bus
        while departure < timestamp:
            departure += bus
        departure_dict.update({bus: departure})

earliest_bus = min(departure_dict, key=departure_dict.get)
print(f"Earliest bus: {earliest_bus}")
min_to_wait = departure_dict[earliest_bus] - timestamp
print(f"Minutes to wait: {min_to_wait}")

solution = earliest_bus * min_to_wait
print(f"Solution: {solution}")
