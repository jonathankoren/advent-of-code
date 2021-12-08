#!/usr/bin/env python3

#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
# gggg    ....    gggg    gggg    ....
#
#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg

# The segments are wired randomly
# In a four digit display, all digits have the same random wiring

# INPUT: Each line is a pattern of all 10 digits, a pipe, and then four more digits
# Use the patterns to deduce what the output numbers are.
#
# OUTPUT how many times do the digits 1, 4, 7, or 8 appear?


import sys

def parse_line(line):
    (ins, outs) = line.split(' | ')
    patterns = list(map(lambda x: ''.join(sorted(x)), ins.strip().split(' ')))
    outputs = list(map(lambda x: ''.join(sorted(x)), outs.strip().split(' ')))
    return (patterns, outputs)

def index_sizes(patterns):
    s2p = {}
    for p in patterns:
        s = len(p)
        if s not in s2p:
            s2p[s] = []
        s2p[s].append(p)
    return s2p

def index_patterns(patterns):
    index = {}
    for p in patterns:
        for c in p:
            if c not in index:
                index[c] = []
            index[c].append(p)
    return index

def init_candidates():
    c = dict.fromkeys(list('abcdefg'))
    for k in c:
        c[k] = []
    return c

# PATTERNS in 0 to 9 order
PATTERNS = [ 'abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
SIZE_TO_PATTERN = index_sizes(PATTERNS)
SEGMENT_INDEX_TO_PATTERN = index_patterns(PATTERNS)

simple_patterns = 0     # digits 1, 4, 7, or 8
with open(sys.argv[1]) as infile:
    for line in infile:
        input2canonical = dict.fromkeys(list('abcdefg'))
        candidates = init_candidates()

        (patterns, outputs) = parse_line(line)
        for o in outputs:
            if len(SIZE_TO_PATTERN[len(o)]) == 1:
                simple_patterns += 1

print(simple_patterns)
