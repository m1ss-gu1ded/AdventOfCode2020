with open("input_13.txt") as file:
    timetable = file.readlines()
timetable = [x.strip() for x in timetable]

timetable = timetable[1].split(",")
timetable = [x.replace("x", "0") for x in timetable]
timetable = [int(x) for x in timetable]

bus_list = []
min_list = []

for bus in timetable:
    if bus == 0:
        pass
    else:
        bus = int(bus)
        index = timetable.index(bus)
        bus_list.append(bus)
        min_list.append(index)
print(bus_list)
print(min_list)


def extgcd(a, b):
    u, v, s, t = 1, 0, 0, 1
    while b != 0:
        q = a // b
        a, b = b, a - q * b
        u, s = s, u - q * s
        v, t = t, v - q * t
    return a, u, v


def chinese_remainder(nn, rr):
    if len(nn) == 1:
        return nn[0], rr[0]
    else:
        k = len(nn) // 2
        m, a = chinese_remainder(nn[:k], rr[:k])
        n, b = chinese_remainder(nn[k:], rr[k:])
        g, u, v = extgcd(m, n)
        x = (b - a) * u % n * m + a
        return m * n, x


solution = chinese_remainder(bus_list, min_list)[0] - chinese_remainder(bus_list, min_list)[1]
print(solution)
