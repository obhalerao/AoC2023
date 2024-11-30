import sys
sys.setrecursionlimit(10000) # lol

#lmao dumb dfs time

grid = [l.strip() for l in open("../input.txt").readlines()]

drs = [1, 0, -1, 0]
dcs = [0, -1, 0, 1]

seen = set()

n = len(grid)
m = len(grid[0])

dirmap = {
    'v': 0,
    '<': 1,
    '^': 2,
    '>': 3
}

invdirmap = {dirmap[i]: i for i in dirmap}

prevs = [[[] for j in i] for i in grid]

maxlen = -1

junctions = set()
edges = {}

for i in range(n):
    for j in range(m):
        if grid[i][j] == '#':
            continue
        isjct = True
        for dr, dc in zip(drs, dcs):
            nr = i + dr
            nc = j + dc
            if 0 <= nr < n and 0 <= nc < m:
                if grid[nr][nc] == '.':
                    isjct = False
                    break
        if isjct:
            junctions.add((i, j))

junctions.add((0, 1))
junctions.add((n-1, m-2))

for i in junctions:
    edges[i] = []

def dfs(sr, sc, r, c, length):
    global grid, seen, junctions, edges

    if (r, c) in junctions and (r, c) != (sr, sc):
        edges[(sr, sc)].append((r, c, length))
        return

    if (r, c) in seen: return
    seen.add((r, c))

    if grid[r][c] != '#':
        for number, (dr, dc) in enumerate(zip(drs, dcs)):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < m:
                if grid[nr][nc] == '#':
                    continue
                else:
                    dfs(sr, sc, nr, nc, length+1)

    seen.remove((r, c))

def dfs2(r, c, length):
    global grid, seen, junctions, edges, maxlen
    if (r, c) in seen: return
    seen.add((r, c))

    if (r, c) == (n-1, m-2):
        maxlen = max(length, maxlen)

    for e in edges[(r, c)]:
        dfs2(e[0], e[1], length+e[2])

    seen.remove((r, c))

for jct in junctions:
    dfs(jct[0], jct[1], jct[0], jct[1], 0)

dfs2(0, 1, 0)

print(maxlen)