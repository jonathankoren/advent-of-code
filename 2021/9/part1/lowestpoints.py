#!/usr/bin/env python3

import sys

def lowest(ocean, i, j):
    t = ocean[i][j]
    for i_offset in range(-1, 2):
        for j_offset in range(-1, 2):
            if (abs(i_offset) - abs(j_offset)) == 0:
                # diagonal, or the center
                continue
            ii = i + i_offset
            jj = j + j_offset
            if (ii < 0) or (ii >= len(ocean)) or (jj < 0) or (jj >= len(ocean[0])):
                # off the map
                continue
            if ocean[ii][jj] <= t:
                return False
    return True



ocean = None
with open(sys.argv[1]) as infile:
    ocean = map(lambda x: list(x), filter(lambda x: x != '', infile.read().split("\n")))
    ocean = map(lambda l: list(map(lambda x: int(x), l)), ocean)
    ocean = list(ocean)

risk = 0
for i in range(len(ocean)):
    for j in range(len(ocean[0])):
        if lowest(ocean, i, j):
            risk += 1 + ocean[i][j]
print(risk)
