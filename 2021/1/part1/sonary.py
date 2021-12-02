#!/usr/bin/env python3

import sys

increases = 0
last = None
for line in sys.stdin:
    cur = int(line)
    if last is not None:
        if (cur - last) > 0:
            increases += 1
    last = cur

print(increases)
