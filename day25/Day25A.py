# copied from geeksforgeeks since i didn't want to reimplement karger's algorithm
import random
from collections import deque

lines = [l.strip() for l in open("../input.txt").readlines()]

stoi = {}


class Graph:

    def __init__(self, v, e):
        self.V = v
        self.E = e

        self.edge = []


# A class to represent a subset for union-find
class subset:
    def __init__(self, p, r):
        self.parent = p
        self.rank = r


def kargerMinCut(graph):
    V = graph.V
    E = graph.E
    edge = graph.edge

    subsets = []

    for v in range(V):
        subsets.append(subset(v, 0))

    vertices = V

    while vertices > 2:

        i = int(100000 * random.random()) % E

        subset1 = find(subsets, edge[i][0])
        subset2 = find(subsets, edge[i][1])

        if subset1 == subset2:
            continue

        else:
            vertices -= 1
            Union(subsets, subset1, subset2)

    cutedges = []
    for i in range(E):
        subset1 = find(subsets, edge[i][0])
        subset2 = find(subsets, edge[i][1])
        if subset1 != subset2:
            cutedges.append(edge[i])

    return cutedges


def find(subsets, i):
    if subsets[i].parent != i:
        subsets[i].parent = find(subsets, subsets[i].parent)

    return subsets[i].parent


def Union(subsets, x, y):
    xroot = find(subsets, x)
    yroot = find(subsets, y)

    if subsets[xroot].rank < subsets[yroot].rank:
        subsets[xroot].parent = yroot
    elif subsets[xroot].rank > subsets[yroot].rank:
        subsets[yroot].parent = xroot


    else:
        subsets[yroot].parent = xroot
        subsets[xroot].rank += 1


# Driver program to test above functions
def main():
    # Let us create following unweighted graph
    # 0------1
    # | \    |
    # |  \   |
    # |   \  |
    # |    \ |
    # 3------2
    V = 4
    E = 5
    graph = Graph(V, E)

    # add edge 0-1
    graph.edge.append((0, 1))

    # add edge 0-2
    graph.edge.append((0, 2))

    # add edge 0-3
    graph.edge.append((0, 3))

    # add edge 1-2
    graph.edge.append((1, 2))

    # add edge 2-3
    graph.edge.append((2, 3))

    r = random.random()
    res = kargerMinCut(graph)
    print("Cut found by Karger's randomized algo is", res)


graph = Graph(0, 0)

idx = 0

for line in lines:
    a, bs = line.split(": ")
    a = a.strip()
    if a not in stoi:
        stoi[a] = idx
        idx += 1
    for b in bs.split():
        if b.strip() not in stoi:
            stoi[b.strip()] = idx
            idx += 1
        graph.edge.append((stoi[a], stoi[b.strip()]))

graph.V = len(stoi)
graph.E = len(graph.edge)

edges = {}

for v in stoi:
    edges[stoi[v]] = []

for a, b in graph.edge:
    edges[a].append(b)
    edges[b].append(a)

ms = float("inf")
mc = []
for x in range(1000):
    r = random.random()
    res = kargerMinCut(graph)
    if len(res) < ms:
        ms = len(res)
        mc = res

stk = [0]
seen = set()
while stk:
    u = stk.pop()
    if u in seen:
        continue
    seen.add(u)
    for v in edges[u]:
        if (u, v) not in mc and (v, u) not in mc:
            stk.append(v)
print(len(seen)*(len(stoi)-len(seen)))