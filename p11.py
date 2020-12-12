from itertools import islice, product

from aocd import data as seat_layout


seat_layout = seat_layout.splitlines()
ROWS = len(seat_layout)
COLS = len(seat_layout[0])

grid1 = {(x,y): col
        for y, row in enumerate(seat_layout)
        for x, col in enumerate(row)}
grid2 = grid1.copy()

changed_state = True
while changed_state:
    changed_state = False
    prev_grid1 = grid1.copy()
    prev_grid2 = grid2.copy()

    for y in range(ROWS):
        for x in range(COLS):
            if (prev_grid1[(x,y)] == '.'
                    and prev_grid2[(x,y)] == '.'):
                continue

            occupied1 = 0
            occupied2 = 0
            for i, j in islice(product((0,1,-1), repeat=2), 1, None):
                dist = 1
                while (seat2 := prev_grid2.get((x+i*dist,y+j*dist))) is not None:
                    if seat2 in ('#', 'L'):
                        break
                    dist += 1

                occupied1 += prev_grid1.get((x+i,y+j)) == '#'
                occupied2 += seat2 == '#'

            if prev_grid1[(x,y)] == 'L' and occupied1 == 0:
                grid1[(x,y)] = '#'
                changed_state = True
            elif prev_grid1[(x,y)] == '#' and occupied1 >= 4:
                grid1[(x,y)] = 'L'
                changed_state = True

            if prev_grid2[(x,y)] == 'L' and occupied2 == 0:
                grid2[(x,y)] = '#'
                changed_state = True
            elif prev_grid2[(x,y)] == '#' and occupied2 >= 5:
                grid2[(x,y)] = 'L'
                changed_state = True

print('Part 1:', sum(seat == '#' for seat in grid1.values()))
print('Part 2:', sum(seat == '#' for seat in grid2.values()))
