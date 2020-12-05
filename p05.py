from aocd import data as boarding_passes


table = str.maketrans('FBLR', '0101')
seats = [int(bp.translate(table), 2) for bp in boarding_passes.splitlines()]
M = min(seats) - 1
L = len(seats) + 1

print('Part 1:', max(seats))
print('Part 2:', (L**2 + L) // 2 + L * M - sum(seats))
