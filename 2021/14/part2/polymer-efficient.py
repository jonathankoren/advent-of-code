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

pair_freqs = {}
for i in range(len(template) - 1):
    pair = template[i] + template[i + 1]
    pair_freqs[pair] = pair_freqs.get(pair, 0) + 1


for step in range(steps):
    new_pair_freqs = {}
    for (p, c) in pair_freqs.items():
        l = p[0]
        r = p[1]
        insert = rules.get(p, '')
        if p in rules:
            new_pair_freqs[l + insert] = new_pair_freqs.get(l + insert, 0) + c
            new_pair_freqs[insert + r] = new_pair_freqs.get(insert + r, 0) + c
    pair_freqs = new_pair_freqs


counts = {}
for (p, c) in pair_freqs.items():
    l = p[0]
    r = p[1]
    counts[l] = counts.get(l, 0) + c
counts[template[-1]] = counts.get(template[-1], 0) + 1


sorted_monomers = sorted(counts.items(), key=lambda p: p[1])
print(sorted_monomers[-1][1] - sorted_monomers[0][1])
