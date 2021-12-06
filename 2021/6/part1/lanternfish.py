#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print('usage: prog <infile> <days>')
    sys.exit(1)

ages = None
infile = open(sys.argv[1])
ages = list(map(lambda x: int(x), infile.read().split(',')))
infile.close()
SIM_DAYS = int(sys.argv[2])

OLD_FISH_RESET = 6
NEW_FISH_RESET = 8

#print('X :::', ages)
resets = [OLD_FISH_RESET] * len(ages)
for day in range(1, SIM_DAYS + 1):
    for i in range(len(ages)):
        ages[i] -= 1
        if ages[i] < 0:
            #print('day', day, 'fish', i, 'spawned. new reset', NEW_FISH_RESET)
            if resets[i] == NEW_FISH_RESET:
                resets[i] = OLD_FISH_RESET
            ages[i] = resets[i]
            resets.append(NEW_FISH_RESET)
    # append the new fish
    #print('NEW FISH', len(resets) - len(ages))
    offset = len(ages)
    for i in range(len(resets) - len(ages)):
        #print(len(ages) + i)
        ages.append(resets[offset + i])
    #print(day, ':::', ages, len(ages))

print(len(ages))
