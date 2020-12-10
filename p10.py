from aocd import data


data = sorted([int(i) for i in data.splitlines()])
one = 1
three = 1
for i, j in zip(data, data[1:]):
    if j - i == 1:
        one += 1
    elif j - i == 3:
        three += 1

print(one*three)
data = [0] + data
adapters = {adapter: 0 for adapter in data}
adapters[data[-1]+3] = 1
for adapter in reversed(data):
    for diff in range(1,4):
        adapters[adapter] += adapters.get(adapter + diff, 0)

print(adapters[0])
