import sys
sys.setrecursionlimit(3000) # lol

grid = [l.strip() for l in open("../input.txt").readlines()]

topsort = []

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

def dfs(r, c):
    global grid, topsort, seen, dirmap, invdirmap
    if (r, c) in seen: return
    seen.add((r, c))

    if grid[r][c] == '.':
        for number, (dr, dc) in enumerate(zip(drs, dcs)):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < m:
                if grid[nr][nc] == '#':
                    continue
                elif grid[nr][nc] == '.':
                    dfs(nr, nc)
                    prevs[nr][nc].append((r, c))
                else:
                    val = dirmap[grid[nr][nc]]
                    if (val + 2) % 4 == number:
                        continue
                    dfs(nr, nc)
                    prevs[nr][nc].append((r, c))
    else:
        number = dirmap[grid[r][c]]
        dfs(r + drs[number], c + dcs[number])
        prevs[r + drs[number]][c + dcs[number]].append((r, c))
    topsort.append((r, c))


dfs(0, 1)

topsort.reverse()

dp = [[0 for j in i] for i in grid]

for (r, c) in topsort:
    dp[r][c] = max((dp[i][j] for i, j in prevs[r][c]), default=0)+1

print(dp[n-1][m-2]-1)