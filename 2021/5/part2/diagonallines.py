#!/usr/bin/env python3

def make_point(csv):
    (x, y) = map(lambda x: int(x), csv.split(','))
    return Point(x, y)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"({self.x}, {self.y})"

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return f"{self.p1} -> {self.p2}"

    def start_x(self):
        return min(self.p1.x, self.p2.x)

    def end_x(self):
        return max(self.p1.x, self.p2.x)

    def start_y(self):
        return min(self.p1.y, self.p2.y)

    def end_y(self):
        return max(self.p1.y, self.p2.y)

    def is_horizontal(self):
        return (self.p1.y == self.p2.y)

    def is_vertical(self):
        return (self.p1.x == self.p2.x)

    def rotate_90(self):
        return Line(Point(self.p1.y, self.p1.x), Point(self.p2.y, self.p2.x))

def coords(l1, l2):
    x1 = l1.p1.x
    y1 = l1.p1.y
    x2 = l1.p2.x
    y2 = l1.p2.y

    x3 = l2.p1.x
    y3 = l2.p2.y
    x4 = l2.p1.x
    y4 = l2.p2.y

    return (x1, y1, x2, y2, x3, y3, x4, y4)

def intersect(l1, l2):
    (x1, y1, x2, y2, x3, y3, x4, y4) = coords(l1, l2)

    d1 = (x1 - x2) * (y3 - y4)
    d2 = (y1 - y2) * (x3 - x4)
    d = d1 - d2

    if d == 0:
        # They're either overlap, or they don't
        return []

    t1 = (x1 - x3) * (y3 - y4)
    t2 = (y1 - y3) * (x3 - x4)
    t = (t1 - t2) / d

    u1 = (x1 - x3) * (y1 - y2)
    u2 = (y1 - y3) * (x1 - x2)
    u3 = (x1 - x2) * (y3 - y4)
    u4 = (y1 - y2) * (x3 - x4)
    u = (u1 - u2) / d

    if (0 <= t) and (t <= 1) and (0 <= u) and (t <= 1):
        px = x1 + (t * (x2 - x1))
        py = y1 + (t * (y2 - y1))
        return [Point(px, py)]

    return []

def overlap(l1, l2, flipped=False):
    if l1.is_horizontal() and l2.is_horizontal():
        # horizontal
        first_line = l1
        second_line = l2
        if l1.start_x() != min(l1.start_x(), l2.start_x()):
            first_line = l2
            second_line = l1

        if (first_line.start_x() <= second_line.start_x()) \
            and (second_line.start_x() <= first_line.end_x()) \
            and l1.start_y() == l2.start_y():
            # overlaps
            overlap_start = second_line.start_x()
            overlap_end = min(first_line.end_x(), second_line.end_x())
            overlap_distance = (overlap_end - overlap_start) + 1

            covered = []
            for new_x in range(overlap_start, overlap_end + 1):
                if flipped:
                    covered.append(Point(first_line.start_y(), new_x))
                else:
                    covered.append(Point(new_x, first_line.start_y()))

            return covered
        else:
            # no overlap
            return []

    elif l1.is_vertical() and l2.is_vertical():
        # rotate and check
        return overlap(l1.rotate_90(), l2.rotate_90(), True)

    elif (l1.is_vertical() and l2.is_horizontal()) \
        or (l1.is_horizontal() and l2.is_vertical()):
        vert = l1
        horiz = l2
        if l1.is_horizontal():
            vert = l2
            horiz = l1
        if ((horiz.start_x() <= vert.start_x()) and (vert.start_x() <= horiz.end_x())) \
            and ((vert.start_y() <= horiz.start_y()) and (horiz.start_y() <= vert.end_y())):
            return [Point(vert.start_x(), horiz.start_y())]
        else:
            # don't overlap
            return []
    else:
        # It should be a single point, but we don't know where
        # FIXME: this is obviously wrong
        print('angled')
        return intersect(l1, l2)

def read_line():
    (p1csv, junk, p2csv) = input().split(' ')
    return Line(make_point(p1csv), make_point(p2csv))


###############################################################################
if __name__ == '__main__':
    lines = []
    while True:
        try:
            lines.append(read_line())
        except EOFError:
            break

    overlaps = set()
    for i in range(len(lines) - 1):
        for j in range(i + 1, len(lines)):
            print('checking', lines[i], lines[j])
            o = overlap(lines[i], lines[j])
            if len(o) > 0:
                print(lines[i], 'overlaps with', lines[j], 'size', len(o), o)
                for p in o:
                    # We do this trick, to so that we get points with the same
                    # coords to hash to the same value, rather than storing the
                    # memory location of the object
                    overlaps.add(str(p))

    print(len(overlaps))
