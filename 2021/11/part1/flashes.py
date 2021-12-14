#!/usr/bin/env python3

import sys

def get_adjacents(x, y):
    ret = []
    for i in range(x - 1, x + 2):
        if i < 0 or i >= 10:
            continue
        for j in range(y - 1, y + 2):
            if j < 0 or j >= 10:
                continue
            if (i != x) or (j != y):
                ret.append((i, j))
    return ret


###############################################################################
if len(sys.argv) != 3:
    print('usage: flashes.py <infile> <steps>')
    sys.exit(1)

energy = []
with open(sys.argv[1]) as infile:
    for line in infile:
        energy.append(list(map(lambda x: int(x), list(line.strip()))))

print(f"Before any step:")
for r in energy:
    print(''.join(map(lambda x: str(x), r)))
print()

total_flashses = 0
for step in range(int(sys.argv[2])):
    # increase energy
    for x in range(10):
        for y in range(10):
            energy[x][y] += 1

    print(f"In step {step + 1}:")
    for r in energy:
        print(''.join(map(lambda x: str(x), r)))
    print()

    # check for flashes
    check_for_flashes = True
    flashed = set()
    while check_for_flashes:
        check_for_flashes = False
        for x in range(10):
            for y in range(10):
                if (energy[x][y] > 9) and ((x, y) not in flashed):
                    print(x,y, 'flashed')
                    flashed.add((x, y))
                    for (i, j) in get_adjacents(x, y):
                        energy[i][j] += 1
                        check_for_flashes = True

    # reset energies for the flashed
    for (x, y) in flashed:
        energy[x][y] = 0

    total_flashses += len(flashed)

    print(f"After step {step + 1}:")
    for r in energy:
        print(''.join(map(lambda x: str(x), r)))
    print()

print(total_flashses)
