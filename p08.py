import re
from typing import Optional

from aocd import data as boot_code


op_pattern = re.compile(r'(\w+) ((?:\+|-)\d+)')


def execute(code: list, must_halt: bool = False) -> Optional[int]:
    acc = 0
    idx = 0
    seen = set()

    while idx < len(code):
        if idx in seen:
            if must_halt:
                return
            return acc

        seen.add(idx)
        op, arg = op_pattern.search(code[idx]).groups()

        if op == 'nop':
            idx += 1
        elif op == 'jmp':
            idx += int(arg)
        elif op == 'acc':
            acc += int(arg)
            idx += 1

    return acc


boot_code = boot_code.splitlines()

acc = execute(boot_code)
print('Part 1:', acc)

for i, op in enumerate(boot_code):
    new_boot_code = boot_code.copy()

    if op.startswith('jmp'):
        new_boot_code[i] = op.replace('jmp', 'nop')
    elif op.startswith('nop'):
        new_boot_code[i] = op.replace('nop', 'jmp')

    acc = execute(new_boot_code, must_halt=True)
    if acc is not None:
        break

print('Part 2:', acc)
