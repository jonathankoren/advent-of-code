#!/usr/bin/env python3

import sys

def sum_window(last_line_num, window):
    sum = 0
    for i in range(last_line_num, last_line_num - len(window) + 1, -1):
        sum += window[i % len(window)]
    return sum


increases = 0
WINDOW_SIZE = 4
window = [None] * WINDOW_SIZE
line_number = 0
for line in sys.stdin:
    window[line_number % WINDOW_SIZE] = int(line)
    if line_number >= 3:
        cur_sum = sum_window(line_number, window)
        prev_sum = sum_window(line_number - 1, window)
        if cur_sum > prev_sum:
            increases += 1
    line_number += 1

print(increases)
