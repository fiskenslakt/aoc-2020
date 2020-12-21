import re
from collections import defaultdict
from itertools import combinations, product

from aocd import data


tiles = defaultdict(dict)
for tile in data.split('\n\n'):
    tile_id, image = tile.split('\n', 1)
    tile_id = int(re.search(r'(\d+)', tile_id)[1])
    L = ''  # Left
    R = ''  # Right
    T = ''  # Top
    B = ''  # Bottom
    for y, row in enumerate(image.splitlines()):
        for x, pixel in enumerate(row):
            tiles[tile_id][(x,y)] = pixel

            if y == 0:
                T += pixel
            elif y == 9:
                B += pixel

            if x == 0:
                L += pixel
            elif x == 9:
                R += pixel

    tiles[tile_id]['T'] = (hash(T), hash(T[::-1]))
    tiles[tile_id]['B'] = (hash(B), hash(B[::-1]))
    tiles[tile_id]['L'] = (hash(L), hash(L[::-1]))
    tiles[tile_id]['R'] = (hash(R), hash(R[::-1]))
    tiles[tile_id]['borders'] = (
        tiles[tile_id]['T'],
        tiles[tile_id]['B'],
        tiles[tile_id]['L'],
        tiles[tile_id]['R'],
    )
    tiles[tile_id]['matches'] = 0

for tile1, tile2 in combinations(tiles.items(), 2):
    for border1, border2 in product(tile1[1]['borders'], tile2[1]['borders']):
        if border1 == border2 or border1 == border2[::-1]:
            tile1[1]['matches'] += 1
            tile2[1]['matches'] += 1

corners_product = 1
for tile_id, tile in tiles.items():
    if tile['matches'] <= 2:
        corners_product *= tile_id

print('Part 1:', corners_product)
