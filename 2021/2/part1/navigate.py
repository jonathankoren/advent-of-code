#!/usr/bin/env python3

import sys

horizontal = 0
depth = 0
for line in sys.stdin:
    (direction, distance) = line.split(' ')
    distance = int(distance)
    if direction == 'forward':
        horizontal += distance
    elif direction == 'down':
        depth += distance
    elif direction == 'up':
        depth -= distance

print(horizontal * depth)
