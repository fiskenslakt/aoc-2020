from functools import reduce
from itertools import combinations
from operator import mul

from aocd import data as expense_report


entries = list(map(int, expense_report.splitlines()))

for part in (1, 2):
    for combo in combinations(entries, part+1):
        if sum(combo) == 2020:
            print(f'Part {part}:', reduce(mul, combo))
            break
