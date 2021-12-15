#!/usr/bin/env python3

import sys
from heapq import heappush, heappop, heapify

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.index = {}

    def add_update(self, item, priority):
        if item in self.index:
            self.index[item][0] = priority
            heapify(self.heap)
        else:
            self.index[item] = [priority, item]
            heappush(self.heap, self.index[item])

    def remove(self):
        (priority, item) = heappop(self.heap)
        del self.index[item]
        return item

    def empty(self):
        return len(self.heap) == 0

def adjacents(r, c, cave):
    adj = []
    for i in range(-1, 2):
        if (r + i < 0) or (r + i >= len(cave)):
            continue
        if i == 0:
            continue
        adj.append((r + i, c))
    for j in range(-1, 2):
        if (c + j < 0) or (c + j >= len(cave[0])):
            continue
        if j == 0:
            continue
        adj.append((r, c + j))
    return adj

def dijkstras(cave):
    pq = PriorityQueue()    # queue of verticies
    dist = {}   # vertex -> distance
    prev = {}   # destination -> source  i.e. vertex - preceeding vertex
    dist[(0,0)] = 0
    pq.add_update((0, 0), 0)

    while (not pq.empty()):
        cur = pq.remove()
        for neighbor in adjacents(cur[0], cur[1], cave):
            alt = dist[cur] + cave[neighbor[0]][neighbor[1]]
            if (neighbor not in dist) or (alt < dist[neighbor]):
                dist[neighbor] = alt
                prev[neighbor] = cur
                pq.add_update(neighbor, alt)

    return (dist, prev)


def mmod(n, mod):
    if n <= mod:
        return n
    if (n % mod) == 0:
        return mod
    return n % mod


smallcave = []
with open(sys.argv[1]) as infile:
    for line in infile:
        smallcave.append(list(map(lambda x: int(x), list(line.strip()))))

# make the cave five times bigger
small_rows = len(smallcave)
small_cols = len(smallcave[0])


cave = [None] * (small_rows * 5)
for i in range(small_rows * 5):
    cave[i] = [None] * (small_cols * 5)

for r in range(small_rows * 5):
    for c in range(small_cols * 5):
        sc = c % small_cols
        sr = r % small_rows
        s = smallcave[sr][sc]
        cave[r][c] = mmod(s + (r // small_rows) + (c // small_cols), 9)




for sr in range(small_rows):
    for sc in range(small_cols):
        for m in range(5):
            r = sr + (small_rows * m)
            c = sc + (small_cols * m)
            cave[r][c] = mmod(smallcave[sr][sc] + (r // small_rows) + (c // small_rows), 9)

#for r in cave:
#    print(''.join(map(lambda x: str(x), r)))






(dist, prev) = dijkstras(cave)

print(dist[(len(cave) - 1, len(cave[0]) - 1)])
