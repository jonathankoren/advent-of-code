#!/usr/bin/env python3

import sys

def binary_to_int(bit_array):
    n = 0
    for i in range(len(bit_array)):
        if i > 0:
            n *= 2
        n += int(bit_array[i])
    return n

one_counts = None
total_lines = 0
num_bits = 0
for line in sys.stdin:
    total_lines += 1
    bit_array = list(map(lambda x: int(x), list(line[:-1])))
    num_bits = len(bit_array)
    if total_lines == 1:
        one_counts = [0] * num_bits
    for i in range(num_bits):
        if bit_array[i] == 1:
            one_counts[i] += 1

most_common_bits = [None] * num_bits
least_common_bits = [None] * num_bits
for i in range(num_bits):
    if one_counts[i] > (total_lines / 2):
        most_common_bits[i] = 1
        least_common_bits[i] = 0
    else:
        most_common_bits[i] = 0
        least_common_bits[i] = 1

gamma_rate = binary_to_int(most_common_bits)
epsilon_rate = binary_to_int(least_common_bits)

print(gamma_rate * epsilon_rate)
