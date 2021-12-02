#!/usr/bin/env python3

import sys

horizontal = 0
depth = 0
aim = 0
for line in sys.stdin:
    (direction, distance) = line.split(' ')
    distance = int(distance)
    if direction == 'forward':
        horizontal += distance
        depth += aim * distance
    elif direction == 'down':
        aim += distance
    elif direction == 'up':
        aim -= distance

print(horizontal * depth)
