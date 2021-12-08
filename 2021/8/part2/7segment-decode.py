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

def index_segment_frequencies(patterns):
    index = {}
    for p in patterns:
        for c in p:
            index[c] = index.get(c, 0) + 1
    return index

def find_patterns_of_size(patterns, size):
    ps = []
    for p in patterns:
        if len(p) == size:
            ps.append(p)
    return ps

def decode_outputs(input2canonical, patterns, PATTERNS_TO_VALUE):
    v = ''
    for p in patterns:
        v += str(decode_pattern(input2canonical, p, PATTERNS_TO_VALUE))
    return int(v)

def decode_pattern(input2canonical, input_pattern, PATTERNS_TO_VALUE):
    canonical_pattern = ''
    for ic in input_pattern:
        canonical_pattern += input2canonical[ic]
    return PATTERNS_TO_VALUE[''.join(sorted(canonical_pattern))]

# PATTERNS in 0 to 9 order
PATTERNS = [ 'abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
PATTERNS_TO_VALUE = {}
for v in range(10):
    PATTERNS_TO_VALUE[PATTERNS[v]] = v


sum = 0
with open(sys.argv[1]) as infile:
    for line in infile:
        input2canonical = {}

        (patterns, outputs) = parse_line(line)

        ic2freqs = index_segment_frequencies(patterns)

        # frequency analysis
        for (ic, freq) in ic2freqs.items():
            if freq == 4:
                # uniquely, canonical segment e occurs 4 times
                input2canonical[ic] = 'e'
            elif freq == 6:
                # uniquely, canonical segment b occurs 6 times
                input2canonical[ic] = 'b'
            elif freq == 9:
                # uniquely, canonical segment f occurs 9 times
                input2canonical[ic] = 'f'

        # canonical segments a and c occur 8 times
        # canonical segments d and g occur 7 times


        # uniquely, one has 2 segments
        # uniquely, seven has 3 segments
        # one and seven differ by the canonical segment a
        one_pattern = find_patterns_of_size(patterns, 2)[0]
        seven_pattern = find_patterns_of_size(patterns, 3)[0]
        input_to_canonical_a = list(set(seven_pattern) - set(one_pattern))[0]
        input2canonical[input_to_canonical_a] = 'a'

        # we can now deduce canonical segement c, as the input that's not
        # locked on one_pattern
        for ic in one_pattern:
            if ic not in input2canonical:
                input2canonical[ic] = 'c'

        # The only segments not decoded are d and g
        # Zero is the only 6 segment that pattern that has d off, and g on.
        # uniqely, eight is the only pattern with all 7 segments
        eight_pattern = find_patterns_of_size(patterns, 7)[0]
        for size_6_pattern in find_patterns_of_size(patterns, 6):
            missing_segment = list(set(eight_pattern) - set(size_6_pattern))[0]
            if missing_segment not in input2canonical:
                input2canonical[missing_segment] = 'd'
                break

        # The only one left to decode is g
        canonical_g = list(set(eight_pattern) - set(input2canonical.keys()))[0]
        input2canonical[canonical_g] = 'g'

        sum += decode_outputs(input2canonical, outputs, PATTERNS_TO_VALUE)

print(sum)
