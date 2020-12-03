from functools import reduce
from operator import mul

from aocd import data


SLOPES = (
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
)

tree_map = data.splitlines()
trees = 0
trees = []
tile_width = len(tree_map[0])

for x, y in SLOPES:
    x_pos = 0
    y_pos = 0
    trees_hit = 0

    while y_pos < len(tree_map):
        if tree_map[y_pos][x_pos % tile_width] == '#':
            trees_hit += 1

        x_pos += x
        y_pos += y

    trees.append(trees_hit)

print('Part 1:', trees[1])
print('Part 2:', reduce(mul, trees))
