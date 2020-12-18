from collections import deque
from operator import add, mul

from aocd import data as homework


def get_infix(expression: str, advanced: bool = False) -> deque:
    ops = []
    queue = deque()

    for token in expression.replace(' ', ''):
        if token.isdigit():
            queue.append(token)
        elif token in ('+', '*'):
            if advanced:
                while ops and ops[-1] == '+':
                    queue.append(ops.pop())
            else:
                while ops and ops[-1] != '(':
                    queue.append(ops.pop())
            ops.append(token)
        elif token == '(':
            ops.append(token)
        elif token == ')':
            while ops[-1] != '(':
                queue.append(ops.pop())
            ops.pop()

    while ops:
        queue.append(ops.pop())

    return queue


operator = {'+': add, '*': mul}

for part2 in (False, True):
    total = 0
    for problem in homework.splitlines():
        stack = []
        queue = get_infix(problem, part2)

        while queue:
            token = queue.popleft()
            if token.isdigit():
                stack.append(token)
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(operator[token](a, b))

        total += stack.pop()

    part = 'Part 2: ' if part2 else 'Part 1: '
    print(f'{part}{total}')
