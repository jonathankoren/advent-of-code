#!/usr/bin/env python3

import functools
import operator
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


def fill_basin(ocean, basins, i, j, basin_id):
    if (i < 0) or (i >= len(ocean)) or (j < 0) or (j >= len(ocean[0])):
        # off map
        return

    if ocean[i][j] == 9:
        # not a basin
        return

    if basins[i][j] > 0:
        # already marked
        return

    basins[i][j] = basin_id
    fill_basin(ocean, basins, i - 1, j, basin_id)
    fill_basin(ocean, basins, i + 1, j, basin_id)
    fill_basin(ocean, basins, i, j - 1, basin_id)
    fill_basin(ocean, basins, i, j + 1, basin_id)


#######################################################
ocean = None
with open(sys.argv[1]) as infile:
    ocean = map(lambda x: list(x), filter(lambda x: x != '', infile.read().split("\n")))
    ocean = map(lambda l: list(map(lambda x: int(x), l)), ocean)
    ocean = list(ocean)

basins = [None] * len(ocean)
for i in range(len(ocean)):
    basins[i] = [0] * len(ocean[0])

# mark the basins
basin_id = 1
for i in range(len(ocean)):
    for j in range(len(ocean[0])):
        if lowest(ocean, i, j):
            fill_basin(ocean, basins, i, j, basin_id)
            basin_id += 1

# measure basins
sizes = {}
for id in range(1, basin_id):
    size = 0
    for row in basins:
        for c in row:
            if c == id:
                size += 1
    sizes[id] = size


print(functools.reduce(operator.mul, map(lambda x: x[1], sorted(sizes.items(), key=lambda item: item[1], reverse=True)[:3])))
