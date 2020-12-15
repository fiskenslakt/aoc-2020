from collections import defaultdict

from aocd import data


# data = '0,3,6'
x = 2020
x = 30_000_000

nums = [int(n) for n in data.split(',')]

memory = defaultdict(list)
for turn, n in enumerate(map(int, nums), 1):
    memory[n].append(turn)

for turn in range(len(nums)+1, x+1):
    prev_n = nums[-1]
    if len(memory[prev_n]) >= 2:
        last, recent = memory[prev_n][-2:]
        new_n = recent - last
        nums.append(new_n)
        memory[new_n].append(turn)
    else:
        nums.append(0)
        memory[0].append(turn)

# print('Part 1:', nums[-1])
print('Part 2:', nums[-1])
