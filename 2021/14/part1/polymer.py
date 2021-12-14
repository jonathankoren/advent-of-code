#!/usr/bin/env python3

import sys


rules = {}
template = None
with open(sys.argv[1]) as infile:
    for line in infile:
        line = line.strip()
        if '->' in line:
            (left, arrow, right) = line.split(' ')
            rules[left] = right
        elif template is None:
            template = line;

steps = int(sys.argv[2])

# construct the polymer
polymer = template
for step in range(steps):
    new_polymer = ''
    for i in range(len(polymer) - 1):
        l = polymer[i]
        r = polymer[i + 1]
        insert = rules.get(l + r, '')
        if i == 0:
            new_polymer = l
        new_polymer += insert + r

    polymer = new_polymer

# count the monomers
counts = {}
for c in polymer:
    counts[c] = counts.get(c, 0) + 1


sorted_monomers = sorted(counts.items(), key=lambda p: p[1])
print(sorted_monomers[-1][1] - sorted_monomers[0][1])
