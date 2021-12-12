#!/usr/bin/env python3

import sys

def printd(s, d):
    tabs = ""
    for i in range(d):
        tabs += "  "
    print(tabs, s)

def dfs(graph, cur, visited, depth=0):
    '''Returns the number of times it reached the end'''
    printd(f"{cur} {visited}", depth)
    if cur == 'end':
        return 1

    v = set()
    for e in visited:
        v.add(e)
    if cur.lower() == cur:
        # is small
        v.add(cur)


    finishes = 0
    stuck = True
    for next in graph[cur]:
        if next in visited:
            continue
        stuck = False
        finishes += dfs(graph, next, v, depth + 1)

    return finishes



#############################################################################

graph = {}

with open(sys.argv[1]) as infile:
    for line in infile:
        (a, b) = line.strip().split('-')
        if a not in graph:
            graph[a] = set()
        if b not in graph:
            graph[b] = set()
        graph[a].add(b)
        graph[b].add(a)

print(dfs(graph, 'start', set()))
