#!/usr/bin/env python3

import sys

def crabfuel(cur, new):
    delta = abs(cur - new)
    return (delta * (delta + 1)) / 2


infile = open(sys.argv[1])
positions = list(map(lambda x: int(x), infile.read().split(',')))
infile.close()

min_pos = min(positions)
max_pos = max(positions)

best_pos = None
best_fuel = None
for p in range(min_pos, max_pos + 1):
    cost = sum(map(lambda x: crabfuel(x, p), positions))
    if (best_fuel is None) or (cost < best_fuel):
        best_fuel = cost
        best_pos = p

print('pos', best_pos, 'fuel', int(best_fuel))
