import re
from itertools import cycle
from typing import List

from aocd import data


def invalid_values(ticket: str) -> List[int]:
    values = [int(n) for n in re.findall(r'(\d+)', ticket)]
    invalid = []

    for value in values:
        for rule in rules:
            a, b, x, y = map(int, rule_pattern.search(rule).groups())
            if a <= value <= b or x <= value <= y:
                break
        else:
            invalid.append(value)

    return invalid


rule_pattern = re.compile(r'(\d+)-(\d+) or (\d+)-(\d+)')

rules = data[:data.find('your')].strip().splitlines()
my_ticket = data[data.find('your'):].strip().splitlines()[1]
nearby_tickets = data[data.find('nearby'):].splitlines()[1:]

invalid = 0
valid_tickets = []

for ticket in nearby_tickets:
    values = invalid_values(ticket)

    if values:
        invalid += sum(values)
    else:
        valid_tickets.append(ticket)

print('Part 1:', invalid)

valid_tickets = [[int(n) for n in re.findall(r'\d+', ticket)] for ticket in valid_tickets]
rule_order = {}
taken = set()
for i, column in cycle(enumerate(zip(*valid_tickets))):
    valid_rules = set(i for i in range(len(rules)) if i not in rule_order)
    invalid_rules = set()

    for num in column:
        for j, rule in enumerate(rules):
            if j in rule_order:
                continue
            a, b, x, y = map(int, rule_pattern.search(rule).groups())
            if not (a <= num <= b) and not (x <= num <= y):
                invalid_rules.add(j)

    rules_left = valid_rules - invalid_rules
    if len(rules_left) == 1:
        rule_order[rules_left.pop()] = i

    if len(rules) == len(rule_order):
        break

departure_fields = [i for i, rule in enumerate(rules) if rule.startswith('departure')]
my_ticket_values = [int(n) for n in re.findall(r'\d+', my_ticket)]
product = 1
for field in departure_fields:
    product *= my_ticket_values[rule_order[field]]

print('Part 2:', product)
