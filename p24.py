import re
from collections import defaultdict

from aocd import data as tile_routes


cardinals = {
    'sw': -.5+.5j,
    'se': .5+.5j,
    'nw': -.5-.5j,
    'ne': .5-.5j,
    'e': 1,
    'w': -1,
}

tiles = defaultdict(bool)

for tile_steps in tile_routes.splitlines():
    pos = 0j
    steps = re.findall(r'(s[we]|n[we]|w|e)', tile_steps)
    for step in steps:
        pos += cardinals[step]

    tiles[pos] = not tiles[pos]

print('Part 1:', sum(tiles.values()))

for day in range(1,101):
    new_tiles = defaultdict(bool)

    for tile, black in tiles.copy().items():
        if black:
            bn_count = sum(tiles[tile+step] for step in cardinals.values())

            if bn_count in (1, 2):
                new_tiles[tile] = True

            for step in cardinals.values():
                neighbor = tile + step
                bn_count = sum(tiles[neighbor+step] for step in cardinals.values())

                if tiles[neighbor] and bn_count in (1, 2):
                    new_tiles[neighbor] = True
                elif not tiles[neighbor] and bn_count == 2:
                    new_tiles[neighbor] = True

    tiles = new_tiles

print('Part 2:', sum(new_tiles.values()))
