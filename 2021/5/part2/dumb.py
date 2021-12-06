#!/usr/bin/env python3

# 20766 is too high

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

    def get_points(self):
        rise = self.p2.y - self.p1.y
        run = self.p2.x - self.p1.x
        points = []
        x = self.p1.x
        y = self.p1.y
        t = 0
        while (x != self.p2.x) or (y != self.p2.y):
            if run > 0:
                x = self.p1.x + t
            elif run < 0:
                x = self.p1.x - t

            if rise > 0:
                y = self.p1.y + t
            elif rise < 0:
                y = self.p1.y - t

            points.append(Point(x, y))
            t += 1

        return points

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

    # keep only horizontal and vertical lines
    #lines = list(filter(lambda l: (l.p1.x == l.p2.x) or (l.p1.y == l.p2.y), lines))

    points = {}
    for line in lines:
        for point in line.get_points():
            h = str(point)
            already = points.get(str(point), 0)
            points[h] = already + 1

    covered = 0
    for (k,v) in points.items():
        if v >= 2:
            covered += 1

    print(covered)
