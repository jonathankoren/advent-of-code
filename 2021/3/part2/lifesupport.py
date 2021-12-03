#!/usr/bin/env python3

import sys

def binary_to_int(bit_array):
    n = 0
    for i in range(len(bit_array)):
        if i > 0:
            n *= 2
        n += int(bit_array[i])
    return n

def find_rating(all_readings, mode, bit=0):
    '''If mode == 1, then calculate the o2 rating by counting the
    most common bits, with 1 winning ties.

    If mode == 0, then calculate the co2 rating by counting the
    least common bits, with 0 winning ties.'''

    one_count = 0
    for bit_array in all_readings:
        if bit_array[bit] == 1:
            one_count += 1

    half = len(all_readings) / 2;
    matching_value = None
    if mode == 1:
        # find the most common bit, with 1s winning ties
        matching_value = int(one_count >= half)
    else:
        # find the least common bit, with 0s winning ties
        matching_value = int(one_count < half)

    filtered = []
    for bit_array in all_readings:
        if bit_array[bit] == matching_value:
            filtered.append(bit_array)

    if len(filtered) == 1:
        return filtered[0]

    return find_rating(filtered, mode, bit + 1)

total_lines = 0
num_bits = 0
all_readings = []
for line in sys.stdin:
    total_lines += 1
    bit_array = list(map(lambda x: int(x), list(line[:-1])))
    num_bits = len(bit_array)
    all_readings.append(bit_array)

o2_rating = binary_to_int(find_rating(all_readings, 1))
co2_rating = binary_to_int(find_rating(all_readings, 0))

print(o2_rating * co2_rating)
