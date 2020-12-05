import re

from aocd import data as policies


valid_sled = 0
valid_toboggan = 0

for policy in policies.splitlines():
    lo, hi, char, pw = re.findall(r'(\w+)', policy)

    valid_sled += int(lo) <= pw.count(char) <= int(hi)
    valid_toboggan += (pw[int(lo)-1] == char) ^ (pw[int(hi)-1] == char)

print('Part 1:', valid_sled)
print('Part 2:', valid_toboggan)
