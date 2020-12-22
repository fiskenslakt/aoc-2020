from collections import deque
from typing import Callable, Tuple

from aocd import data as space_cards


def cache(f: Callable) -> Callable:
    _cache = {}
    def inner(p1: tuple, p2: tuple) -> Tuple[str, deque]:
        game = get_game_hash(p1, p2)
        if game not in _cache:
            winner, deck = f(p1, p2)
            _cache[game] = (winner, deck)

        return _cache[game]

    inner.seen = set()
    return inner


def get_game_hash(p1: deque, p2: deque) -> int:
    p1 = tuple(p1)
    p2 = tuple(p2)
    return hash((p1, p2))


@cache
def recursive_combat(p1: Tuple[int], p2: Tuple[int]) -> Tuple[str, deque]:
    p1 = deque(p1)
    p2 = deque(p2)

    while p1 and p2:
        game = get_game_hash(p1, p2)
        if game in recursive_combat.seen:
            return 'p1', p1
        else:
            recursive_combat.seen.add(game)

        top1, top2 = p1.popleft(), p2.popleft()

        if len(p1) >= top1 and len(p2) >= top2:
            winner, deck = recursive_combat(tuple(p1)[:top1], tuple(p2)[:top2])

            if winner == 'p1':
                p1.append(top1)
                p1.append(top2)
            elif winner == 'p2':
                p2.append(top2)
                p2.append(top1)

        elif top1 > top2:
            p1.append(top1)
            p1.append(top2)
        elif top2 > top1:
            p2.append(top2)
            p2.append(top1)

    winner = 'p1' if p1 else 'p2'
    deck = p1 if p1 else p2

    return winner, deck


p1, p2 = space_cards.split('\n\n')

p1 = deque([int(card) for card in p1.splitlines()[1:]])
p2 = deque([int(card) for card in p2.splitlines()[1:]])

p1p2 = tuple(p1)
p2p2 = tuple(p2)

while p1 and p2:
    top1, top2 = p1.popleft(), p2.popleft()

    if top1 > top2:
        p1.append(top1)
        p1.append(top2)
    elif top2 > top1:
        p2.append(top2)
        p2.append(top1)

winner = p1 if p1 else p2
print('Part 1:', sum(i*card for i, card in enumerate(reversed(winner), 1)))

_, winner = recursive_combat(p1p2, p2p2)
print('Part 2:', sum(i*card for i, card in enumerate(reversed(winner), 1)))
