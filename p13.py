import re

from aocd import data as notes


timestamp, buses = notes.splitlines()

timestamp = int(timestamp)
bus_ids = [int(bus) for bus in re.findall(r'\d+', buses)]

t = timestamp
while True:
    for bus in bus_ids:
        if t % bus == 0:
            earliest_departure = t
            break
    else:
        t += 1
        continue
    break

print('Part 1:', (earliest_departure - timestamp) * bus)

remainders = []
for i, bus in enumerate(buses.split(',')):
    if bus != 'x':
        remainders.append(-i % int(bus))

t = 0
while not all(t % bus == rem for bus, rem in zip(bus_ids, remainders)):
    step = 1
    for bus, rem in zip(bus_ids, remainders):
        if t % bus == rem:
            step *= bus

    t += step

print('Part 2:', t)
