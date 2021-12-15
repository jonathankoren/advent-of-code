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



cave = []
with open(sys.argv[1]) as infile:
    for line in infile:
        cave.append(list(map(lambda x: int(x), list(line.strip()))))

(dist, prev) = dijkstras(cave)

print(dist[(len(cave) - 1, len(cave[0]) - 1)])
