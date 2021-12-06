#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print('usage: prog <infile> <days>')
    sys.exit(1)

infile = open(sys.argv[1])
initial_ages = list(map(lambda x: int(x), infile.read().split(',')))
infile.close()
SIM_DAYS = int(sys.argv[2])

OLD_FISH_RESET = 6
NEW_FISH_RESET = 8


counters = [0] * (NEW_FISH_RESET + 1)
for age in initial_ages:
    counters[age] += 1

#print('X :::', counters)
for day in range(1, SIM_DAYS + 1):
    new_counters = [0] * (NEW_FISH_RESET + 1)
    for age in range(NEW_FISH_RESET + 1):
        if age == 0:
            new_counters[NEW_FISH_RESET] = counters[0]
            new_counters[OLD_FISH_RESET] = counters[0]
        else:
            new_counters[age - 1] += counters[age]
    counters = new_counters
    #print(day, ':::', counters)

print(counters)
print(sum(counters))
