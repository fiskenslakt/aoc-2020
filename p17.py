from collections import defaultdict
from itertools import islice, product

from aocd import data as starting_region


grid = defaultdict(lambda: '.')

for y, row in enumerate(starting_region.splitlines()):
    for x, cube in enumerate(row):
        grid[(x,y,0,None)] = cube
        grid[(x,y,0,0)] = cube

        # initialize neighbors
        for i, j, k in product((0,1,-1), repeat=3):
            grid[(x+i,y+j,k,None)]
        for i, j, k, m in product((0,1,-1), repeat=4):
            grid[(x+i,y+j,k,m)]

for cycle in range(6):
    prev_grid = grid.copy()

    for x, y, z, w in prev_grid.copy():
        active_3d = 0
        active_4d = 0

        if w is None:
            for i, j, k in islice(product((0,1,-1), repeat=3), 1, None):
                # initialize neighbors
                grid[(x+i,y+j,z+k,None)]
                active_3d += prev_grid[(x+i,y+j,z+k,None)] == '#'
        else:
            for i, j, k, m in islice(product((0,1,-1), repeat=4), 1, None):
                # initialize neighbors
                grid[(x+i,y+j,z+k,m+w)]
                active_4d += prev_grid[(x+i,y+j,z+k,m+w)] == '#'

        if w is None:
            if prev_grid[(x,y,z,None)] == '#' and active_3d not in (2, 3):
                grid[(x,y,z,None)] = '.'
            elif prev_grid[(x,y,z,None)] == '.' and active_3d == 3:
                grid[(x,y,z,None)] = '#'
        else:
            if prev_grid[(x,y,z,w)] == '#' and active_4d not in (2, 3):
                grid[(x,y,z,w)] = '.'
            elif prev_grid[(x,y,z,w)] == '.' and active_4d == 3:
                grid[(x,y,z,w)] = '#'

print('Part 1:', sum(cube == '#' for coord, cube in grid.items() if coord[-1] is None))
print('Part 2:', sum(cube == '#' for coord, cube in grid.items() if coord[-1] is not None))
