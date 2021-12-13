#!/usr/bin/env python3

import sys

def print_dots(dots):
    max_x  = 0
    max_y = 0
    for (x, y) in dots:
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    grid = [None] * (max_y + 1)
    for i in range(max_y + 1):
        grid[i] = ['.'] * (max_x + 1)
    for (x, y) in dots:
        grid[y][x] = '#'
    for row in grid:
        print(''.join(row))
    print()


dots = []
folds = []
with open(sys.argv[1]) as infile:
    read_points = True
    for line in infile:
        line = line.strip()
        if line == '':
            read_points = False
        else:
            if read_points:
                dots.append(list(map(lambda x: int(x), line.split(','))))
            else:
                (axis, value) = line.split(' ')[2].split('=')
                value = int(value)
                folds.append((axis, value))
#print_dots(dots)

for (axis, value) in folds:
    new_dots = []
    for (orig_x, orig_y) in dots:
        if axis == 'x':
            if orig_x > value:
                move = orig_x - value
                new_dots.append((value - move, orig_y))
            else:
                new_dots.append((orig_x, orig_y))
        else:
            if orig_y > value:
                move = orig_y - value
                new_dots.append((orig_x, value - move))
            else:
                new_dots.append((orig_x, orig_y))
    dots = new_dots
    break
    #print_dots(dots)

print(len(set(dots)))
