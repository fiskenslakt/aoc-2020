from itertools import combinations

from aocd import data


nums = [int(n) for n in data.splitlines()]

for i, n in enumerate(nums[25:], 25):
    for combo in combinations(nums[i-25:i], 2):
        if sum(combo) == n:
            break
    else:
        print(n)
        x = n

for i in range(2, len(nums)-2):
    for j in range(len(nums)-i):
        if sum(nums[j:j+i]) == x:
            y = nums[j:j+i]
            print(min(y)+max(y))
            raise SystemExit
