import re

from aocd import data as rules


def can_contain_gold(outer_bag: str) -> bool:
    for qty, bag in graph[outer_bag]:
        if bag == 'shiny gold':
            return True
        elif can_contain_gold(bag):
            return True
    return False


def bag_load(outer_bag: str) -> int:
    for qty, bag in graph[outer_bag]:
        yield int(qty)
        for _ in range(int(qty)):
            yield from bag_load(bag)


graph = {}
bag_types = []
contain_pattern = re.compile(r'(\d+) (\w+ \w+) bags?')

for rule in rules.splitlines():
    outer_bag = rule.split(' bags')[0]
    bag_types.append(outer_bag)
    graph[outer_bag] = contain_pattern.findall(rule)

print('Part 1:', sum(can_contain_gold(bag) for bag in bag_types))
print('Part 2:', sum(qty for qty in bag_load('shiny gold')))
