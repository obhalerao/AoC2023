from collections import deque
from copy import copy
from shapely.geometry import Polygon
lines = [l.strip() for l in open("../input.txt").readlines()]

grid = [[i for i in j] for j in lines]

ngrid = [['.' for i in range(len(grid[0])+2)]]
for i in grid:
    ni = ['.']
    for j in i: ni.append(j)
    ni.append('.')
    ngrid.append(ni)
ngrid.append(ngrid[0])

grid = ngrid

drs = [0, 1, 0, -1]
dcs = [1, 0, -1, 0]

# 0 is right
# 1 is down
# 2 is left
# 3 is up



start = None
for idx, i in enumerate(grid):
    for idx2, j in enumerate(i):
        if j == 'S':
            start = (idx, idx2)
            break

q = deque()

maxdist = 1

seen = {start}

dists = [[0 for i in j] for j in grid]

dists[start[0]][start[1]] = -1

loopset = set()

nbrs = {}

loopset.add(start)

startnbrs = set()

for idx, (dr, dc) in enumerate(zip(drs, dcs)):
        nr = start[0] + dr
        nc = start[1] + dc
        if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]):
            q.append(((nr, nc), idx, 1))
            startnbrs.add((nr, nc))
iter = 4
while q:
    cur = q.popleft()
    coords = cur[0]
    r = coords[0]
    c = coords[1]
    dir = cur[1]
    dist = cur[2]
    ch = grid[coords[0]][coords[1]]
    if ((r, c)) in seen:
        continue
    seen.add(((r, c)))
    dists[r][c] = dist
    loop = False
    if ch == 'J':
        if dir == 0:
            loop = True
            nr = r+drs[3]
            nc = c+dcs[3]
            if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]):
                q.append(((nr, nc), 3, dist + 1))
                if (r, c) not in nbrs:
                    nbrs[(r, c)] = set()
                nbrs[(r, c)].add((nr, nc))
        elif dir == 1:
            loop = True
            nr = r + drs[2]
            nc = c + dcs[2]
            if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]):
                q.append(((nr, nc), 2, dist + 1))
            if (r, c) not in nbrs:
                nbrs[(r, c)] = set()
            nbrs[(r, c)].add((nr, nc))
    if ch == '7':
        if dir == 0:
            loop = True
            nr = r+drs[1]
            nc = c+dcs[1]
            if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]):
                q.append(((nr, nc), 1, dist + 1))
            if (r, c) not in nbrs:
                nbrs[(r, c)] = set()
            nbrs[(r, c)].add((nr, nc))
        elif dir == 3:
            loop = True
            nr = r + drs[2]
            nc = c + dcs[2]
            if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]):
                q.append(((nr, nc), 2, dist + 1))
            if (r, c) not in nbrs:
                nbrs[(r, c)] = set()
            nbrs[(r, c)].add((nr, nc))
    if ch == 'F':
        if dir == 3:
            loop = True
            nr = r+drs[0]
            nc = c+dcs[0]
            if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]):
                q.append(((nr, nc), 0, dist + 1))
            if (r, c) not in nbrs:
                nbrs[(r, c)] = set()
            nbrs[(r, c)].add((nr, nc))
        elif dir == 2:
            loop = True
            nr = r + drs[1]
            nc = c + dcs[1]
            if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]):
                q.append(((nr, nc), 1, dist + 1))
            if (r, c) not in nbrs:
                nbrs[(r, c)] = set()
            nbrs[(r, c)].add((nr, nc))
    if ch == 'L':
        if dir == 1:
            loop = True
            nr = r+drs[0]
            nc = c+dcs[0]
            if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]):
                q.append(((nr, nc), 0, dist + 1))
            if (r, c) not in nbrs:
                nbrs[(r, c)] = set()
            nbrs[(r, c)].add((nr, nc))
        elif dir == 2:
            loop = True
            nr = r + drs[3]
            nc = c + dcs[3]
            if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]):
                q.append(((nr, nc), 3, dist + 1))
            if (r, c) not in nbrs:
                nbrs[(r, c)] = set()
            nbrs[(r, c)].add((nr, nc))
    if ch == '-':
        if dir == 0:
            loop = True
            nr = r+drs[0]
            nc = c+dcs[0]
            if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]):
                q.append(((nr, nc), 0, dist + 1))
            if (r, c) not in nbrs:
                nbrs[(r, c)] = set()
            nbrs[(r, c)].add((nr, nc))
        elif dir == 2:
            loop = True
            nr = r + drs[2]
            nc = c + dcs[2]
            if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]):
                q.append(((nr, nc), 2, dist + 1))
            if (r, c) not in nbrs:
                nbrs[(r, c)] = set()
            nbrs[(r, c)].add((nr, nc))
    if ch == '|':
        if dir == 1:
            loop = True
            nr = r+drs[1]
            nc = c+dcs[1]
            if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]):
                q.append(((nr, nc), 1, dist + 1))
            if (r, c) not in nbrs:
                nbrs[(r, c)] = set()
            nbrs[(r, c)].add((nr, nc))
        elif dir == 3:
            loop = True
            nr = r + drs[3]
            nc = c + dcs[3]
            if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]):
                q.append(((nr, nc), 3, dist + 1))
            if (r, c) not in nbrs:
                nbrs[(r, c)] = set()
            nbrs[(r, c)].add((nr, nc))
    if loop:
        maxdist = max(maxdist, dist)
        loopset.add((r, c))
        if iter > 0:
            if start not in nbrs:
                nbrs[start] = set()
            nbrs[start].add((r, c))
    else:
        seen.remove((r, c))
    iter-=1

keys = set(nbrs.keys())
for k in keys:
    val = nbrs[k]
    for v in val:
        if v not in nbrs:
            nbrs[v] = set()
keys = nbrs.keys()
for k in keys:
    val = nbrs[k]
    for v in val:
        nbrs[v].add(k)

cpt = start
prev = None
pts = []
while True:
    pts.append(cpt)
    for elem in nbrs[cpt]:
        if elem != prev:
            prev = cpt
            cpt = elem
            break
    if cpt == start:
        break
pgon = Polygon(pts)
print(int(pgon.area) - len(pts)/2 + 1)