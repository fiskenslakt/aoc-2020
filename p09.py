from itertools import combinations

from aocd import data as xmas


numbers = [int(n) for n in xmas.splitlines()]

for i, n in enumerate(numbers[25:], 25):
    for combo in combinations(numbers[i-25:i], 2):
        if sum(combo) == n:
            break
    else:
        invalid_number = n

for i in range(2, len(numbers)-2):
    for j in range(len(numbers)-i):
        if sum(numbers[j:j+i]) == invalid_number:
            contiguous_set = numbers[j:j+i]
            break
    else:
        continue
    break

print('Part 1:', invalid_number)
print('Part 2:', min(contiguous_set) + max(contiguous_set))
