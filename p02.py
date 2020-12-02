import re
from collections import Counter

from aocd import data as policies


valid_sled = 0
valid_toboggan = 0

for policy in policies.splitlines():
    policy = re.findall(r'(\w+)', policy)
    low = int(policy[0])
    high = int(policy[1])
    letter = policy[2]
    password = policy[3]
    frequency = Counter(password)

    if low <= frequency[letter] <= high:
        valid_sled += 1

    if (password[low-1] == letter) ^ (password[high-1] == letter):
        valid_toboggan += 1

print('Part 1:', valid_sled)
print('Part 2:', valid_toboggan)
