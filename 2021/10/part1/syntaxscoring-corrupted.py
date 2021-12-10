#!/usr/bin/env python3

import sys

SCORING = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

def closing(c):
    if c == '(':
        return ')'
    elif c == '[':
        return ']'
    elif c == '{':
        return '}'
    elif c == '<':
        return '>'
    raise ValueError

score = 0
with open(sys.argv[1]) as infile:
    for line in infile:
        line = line.strip()
        depth = 0
        stack = []
        for c in line:
            if c in '([{<':
                # opening
                depth += 1
                stack.append(closing(c))
            else:
                # closing
                depth -= 1
                expected = stack.pop()
                if c != expected:
                    # corrupted
                    score += SCORING[c]
                    break
        if depth > 0:
            # incomplete
            pass

print(score)
