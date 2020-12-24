from typing import Iterable

from aocd import data as cup_labels


class Cup:
    def __init__(self, value: int):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'Cup({self.value})'


class Cups:
    def __init__(self):
        self.locate = {}
        self.current = None
        self.destination = None
        self.MAX_CUP_VALUE = float('-inf')

    def __str__(self):
        cup = self.current
        s = f'({cup.value})'
        while cup.next != self.current:
            cup = cup.next
            s += f'->{cup.value}'

        return s

    def pick_up_three(self):
        first_cup = self.current.next
        third_cup = first_cup.next.next

        self.current.next = third_cup.next
        third_cup.next = None

        return first_cup

    def insert_after_dest(self, first_cup: Cup):
        dest = self.destination
        fourth_cup = dest.next
        dest.next = first_cup

        second_cup = first_cup.next
        third_cup = second_cup.next

        third_cup.next = fourth_cup

    @classmethod
    def from_iterable(cls, iterable: Iterable):
        cups = cls()
        iterable = iter(iterable)
        cup = Cup(int(next(iterable)))
        cups.current = cup
        cups.locate[cup.value] = cup
        cups.MAX_CUP_VALUE = max(cups.MAX_CUP_VALUE, cup.value)

        for n in iterable:
            cup.next = Cup(int(n))
            cup = cup.next
            cups.locate[cup.value] = cup
            cups.MAX_CUP_VALUE = max(cups.MAX_CUP_VALUE, cup.value)

        # connect last cup to first cup
        cup.next = cups.current

        return cups


def cup_game(moves: int, cups: Cups):
    for _ in range(moves):
        first_cup = cups.pick_up_three()
        second_cup = first_cup.next
        third_cup = second_cup.next

        next_destination = cups.current.value - 1 or cups.MAX_CUP_VALUE
        while True:
            if next_destination in (first_cup.value, second_cup.value, third_cup.value):
                next_destination -= 1
                if next_destination < 1:
                    next_destination = cups.MAX_CUP_VALUE
                continue

            cups.destination = cups.locate[next_destination]
            break

        cups.insert_after_dest(first_cup)
        cups.current = cups.current.next


cups = Cups.from_iterable(cup_labels)

cup_game(100, cups)

ans = ''
cup = cups.locate[1]
while cup.next.value != 1:
    cup = cup.next
    ans += str(cup.value)
print('Part 1:', ans)

cups = list(cup_labels) + list(range(10, 1_000_001))
cups = Cups.from_iterable(cups)
cup_game(10_000_000, cups)

cup_one = cups.locate[1]
cup_two = cup_one.next
cup_three = cup_two.next
print('Part 2:', cup_two.value * cup_three.value)
