from aocd import data as groups


questions_unique = 0
questions_common = 0

for group in groups.split('\n\n'):
    people = group.splitlines()
    questions_unique += len(set(''.join(people)))
    questions_common += len(set.intersection(*map(set, people)))

print('Part 1:', questions_unique)
print('Part 2:', questions_common)
