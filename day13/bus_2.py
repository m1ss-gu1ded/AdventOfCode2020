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
print(f"divisor list: {bus_list}")
print(f"modulo list: {min_list}")


# extended greatest common divisor: Extended Euclidean algorithm
def extgcd(a, b):
    u, v, s, t = 1, 0, 0, 1
    while b != 0:
        q = a // b
        a, b = b, a - q * b
        u, s = s, u - q * s
        v, t = t, v - q * t
    return a, u, v


# returns dividend m*n and rest x
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


# Since the solution is the smallest number in the set of Chinese remainders: s * 1 = m*n - x
solution = chinese_remainder(bus_list, min_list)[0] - chinese_remainder(bus_list, min_list)[1]
print(f"dividend: {chinese_remainder(bus_list, min_list)[0]}")
print(f"rest: {chinese_remainder(bus_list, min_list)[1]}")
print(f"solution: {solution}")
