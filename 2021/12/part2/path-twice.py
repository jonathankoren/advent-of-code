#!/usr/bin/env python3

import sys

def printd(s, d):
    tabs = ""
    for i in range(d):
        tabs += "  "
    #print(tabs, s)

def is_small(name):
    return name.lower() == name

def dfs(graph, cur, visited, depth=0):
    '''Returns the number of times it reached the end'''
    printd(f"{cur} {visited}", depth)
    if cur == 'end':
        return 1

    v = {}
    any_twice = False
    for (k,kv) in visited.items():
        v[k] = kv
        if kv == 2:
            any_twice = True
    if is_small(cur):
        if any_twice and (v.get(cur, 0) == 1):
            return 0
        v[cur] = v.get(cur, 0) + 1


    finishes = 0
    stuck = True
    for next in graph[cur]:
        if is_small(next):
            if next == 'start':
                continue
            if (v.get(next, 0) >= 2):
                continue
            if (v.get(next, 0) == 1) and any_twice:
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

print(dfs(graph, 'start', {}))
