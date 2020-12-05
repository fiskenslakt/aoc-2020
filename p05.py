from aocd import data as boarding_passes


table = str.maketrans('FBLR', '0101')
seats = []

for boarding_pass in boarding_passes.splitlines():
    seats.append(int(boarding_pass.translate(table), 2))

print('Part 1:', max(seats))
my_seat = set(range(min(seats), max(seats))) - set(seats)
print('Part 2:', my_seat.pop())
