#!/usr/bin/env python3

import sys

SCORING = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
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

scores = []
with open(sys.argv[1]) as infile:
    for line in infile:
        line = line.strip()
        stack = []
        for c in line:
            abort = False
            if c in '([{<':
                # opening
                stack.append(closing(c))
            else:
                # closing
                expected = stack.pop()
                if c != expected:
                    # corrupted
                    abort = True
                    break
            if abort:
                break
        if (not abort) and (len(stack) > 0):
            # incomplete
            line_score = 0
            stack.reverse()
            for c in stack:
                line_score *= 5
                line_score += SCORING[c]
            scores.append(line_score)


scores = sorted(scores)
print(scores[int(len(scores) / 2)])
