#!/usr/bin/env python3

import math
import re
import sys

class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.parent = None

        if type(self.left) == Node:
            self.left.parent = self

        if type(self.right) == Node:
            self.right.parent = self

    def __repr__(self):
        return '[' + repr(self.left) + ',' + repr(self.right) + ']'

    def magnitude(self):
        lv = self.left
        if type(lv) != int:
            lv = self.left.magnitude()
        rv = self.right
        if type(rv) != int:
            rv = self.right.magnitude()
        return (3 * lv) + (2 * rv)

    def _resolve_explosion_up_left(self, v, caller):
        if type(self.left) == int:
            self.left += v
            return True
        elif caller != self.left:
            if self.left._resolve_explosion_down_right(v, self):
                # success!
                return True

        if self.parent is not None:
            return self.parent._resolve_explosion_up_left(v, self)
        else:
            if (caller != self.left) and (type(self.left) == Node):
                return self.left._resolve_explosion_down_right(v, self)
            else:
                return False

    def _resolve_explosion_up_right(self, v, caller):
        if type(self.right) == int:
            self.right += v
            return True
        elif caller != self.right:
            if self.right._resolve_explosion_down_left(v, self):
                # success!
                return True

        if self.parent is not None:
            return self.parent._resolve_explosion_up_right(v, self)
        else:
            if (caller != self.right) and (type(self.right) == Node):
                return self.right._resolve_explosion_down_left(v, self)
            else:
                return False



    def _resolve_explosion_down_left(self, v, caller):
        if type(self.left) == int:
            self.left += v
            return True
        else:
            if self.left._resolve_explosion_down_left(v, self):
                return True
            elif type(self.right) == Node:
                return self.right._resolve_explosion_down_left(v, self)
            else:
                return False

    def _resolve_explosion_down_right(self, v, caller):
        if type(self.right) == int:
            self.right += v
            return True
        else:
            if self.right._resolve_explosion_down_right(v, self):
                return True
            elif type(self.left) == Node:
                return self.left._resolve_explosion_down_right(v, self)
            else:
                return False

    def explode(self, depth=0):
        if depth < 3:
            if (type(self.left) == Node) and self.left.explode(depth + 1):
                return True
            if (type(self.right) == Node):
                return self.right.explode(depth + 1)
            else:
                return False

        # depth 3 check if your children explode
        if type(self.left) == Node:
            # explode your left
            lv = self.left.left
            rv = self.left.right

            # absorb the right number
            if type(self.right) == int:
                self.right += rv
            else:
                self.right._resolve_explosion_down_left(rv, self)

            # absorb the left number
            self.parent._resolve_explosion_up_left(lv, self)
            self.left = 0
            return True

        elif type(self.right) == Node:
            # explode your right
            lv = self.right.left
            rv = self.right.right

            # absorb the left number
            if type(self.left) == int:
                self.left += lv
            else:
                self.right._resolve_explosion_down_right(lv, self)

            # absorb the right number
            self.parent._resolve_explosion_up_right(rv, self)
            self.right = 0
            return True

        return False

    def split(self):
        did_something = False
        if type(self.left) == int:
            if self.left > 9:
                num = self.left
                self.left = Node(int(math.floor(num / 2.0)), int(math.ceil(num / 2.0)))
                self.left.parent = self
                did_something = True
        else:
            did_something = self.left.split()

        if did_something:
            return True

        if type(self.right) == int:
            if self.right > 9:
                num = self.right
                self.right = Node(int(math.floor(num / 2.0)), int(math.ceil(num / 2.0)))
                self.right.parent = self
                return True
        else:
            return self.right.split()


def make_tree(line):
    if (line[0] != '[') and (line[0] != ']'):
        d = re.match('^\d+', line).group(0)
        return (int(d), len(d))
    else:
        (left, loffset) = make_tree(line[1:])
        (right, roffset) = make_tree(line[loffset + 2:]) # +2 for [ and ,
        return (Node(left, right), loffset + roffset + 3)

class Equation:
    def __init__(self, root):
        self.root = root

    def add(self, right):
        self.root = Node(self.root, right)

    def reduce(self):
        while True:
            did_something = self.root.explode()
            if did_something:
                continue

            if not did_something:
                did_something = self.root.split()
            if not did_something:
                break
            else:
                continue

    def magnitude(self):
        return self.root.magnitude()

    def __repr__(self):
        return repr(self.root)

##############################################################################

equation = None
with open(sys.argv[1]) as infile:
    for line in infile:
        tree = make_tree(line.strip())[0]
        if equation is None:
            equation = Equation(tree)
        else:
            # add
            equation.add(tree)
            equation.reduce()


print(repr(equation))
print(equation.root.magnitude())
