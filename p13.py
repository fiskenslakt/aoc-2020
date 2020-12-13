import re

from aocd import data


# data = '''939
# 7,13,x,x,59,x,31,19'''


timestamp, bus_ids = data.splitlines()

timestamp = int(timestamp)
bus_ids = [int(bus) for bus in re.findall(r'\d+', bus_ids)]

i = timestamp
while True:
    for bus in bus_ids:
        if i % bus == 0:
            depart = i
            break
    else:
        i += 1
        continue
    break

ans = (depart - timestamp) * bus
print('Part 1:', ans)
