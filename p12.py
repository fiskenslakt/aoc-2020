import re
from collections import deque

from aocd import data


# data = '''F10
# N3
# F7
# R90
# F11'''


p = re.compile(r'(\w)(\d+)')

facing = deque(['E', 'S', 'W', 'N'])
pos = 0j
waypoint = 10-1j
# 1+10j R90 complex(-imag, real)
# -1-10j L90 complex(imag, -real)
# -10+1j L180/R180 complex(-real, -imag)

for i in data.splitlines():
    m = p.search(i)
    d = m[1]
    a = int(m[2])

    if d == 'N':
        # pos -= 1j*a
        waypoint -= 1j*a
    elif d == 'E':
        # pos += 1*a
        waypoint += 1*a
    elif d == 'S':
        # pos += 1j*a
        waypoint += 1j*a
    elif d == 'W':
        # pos -= 1*a
        waypoint -= 1*a
    elif d == 'F':
        pos = complex(pos.real+waypoint.real*a, pos.imag+waypoint.imag*a)
        # if facing[0] == 'N':
        #     pos -= 1j*a
        # elif facing[0] == 'E':
        #     pos += 1*a
        # elif facing[0] == 'S':
        #     pos += 1j*a
        # elif facing[0] == 'W':
        #     pos -= 1*a
    elif d == 'L':
        # facing.rotate(a//90)
        if a == 90:
            waypoint = complex(waypoint.imag, -waypoint.real)
        elif a == 180:
            waypoint = complex(-waypoint.real, -waypoint.imag)
        elif a == 270:
            waypoint = complex(-waypoint.imag, waypoint.real)
    elif d == 'R':
        # facing.rotate(-a//90)
        if a == 90:
            waypoint = complex(-waypoint.imag, waypoint.real)
        elif a == 180:
            waypoint = complex(-waypoint.real, -waypoint.imag)
        elif a == 270:
            waypoint = complex(waypoint.imag, -waypoint.real)


# print('Part 1:', abs(pos.real) + abs(pos.imag))
print('Part 2:', int(abs(pos.real) + abs(pos.imag)), pos)
