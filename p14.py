import re
from itertools import product, zip_longest

from aocd import data as program


mask_pattern = re.compile(r'([01X]+)')
mem_pattern = re.compile(r'(\d+).+?(\d+)')

memory1 = {}
memory2 = {}

for line in program.splitlines():
    if line.startswith('mask'):
        current_mask = mask_pattern.search(line)[1]
        continue

    address, value = mem_pattern.search(line).groups()
    new_value = ''
    new_address = ''
    vbits = reversed(bin(int(value))[2:])
    abits = reversed(bin(int(address))[2:])
    mbits = current_mask[::-1]

    for vb, mb in zip_longest(vbits, mbits, fillvalue='0'):
        new_value += vb if mb == 'X' else mb

    for ab, mb in zip_longest(abits, mbits, fillvalue='0'):
        new_address += ab if mb == '0' else mb

    memory1[address] = int(new_value[::-1], 2)

    for fb in product('01', repeat=new_address.count('X')):
        address = ''
        fb = iter(fb)
        for bit in new_address:
            address += bit if bit != 'X' else next(fb)

        address = int(address[::-1], 2)
        memory2[address] = int(value)

print('Part 1:', sum(memory1.values()))
print('Part 2:', sum(memory2.values()))
