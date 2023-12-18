from heapq import heappush, heappop

lines = [l.strip() for l in open("../input.txt").readlines()]

grid = [[int(i) for i in j] for j in lines]

def valid(r, c):
    global grid
    return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])

drs = [0,1,0,-1]
dcs = [1,0,-1,0]

RIGHT=0
DOWN=1
LEFT=2
UP=3

pq = []

minHeat = [[[[float("inf") for qq in range(11)] for q in range(4)] for i in j] for j in grid]
minHeat[0][0][RIGHT][0] = 0
minHeat[0][0][DOWN][0] = 0
# heat, r, c, dir, number of blocks moved
heappush(pq, (0, 0, 0, RIGHT, 0))
heappush(pq, (0, 0, 0, DOWN, 0))
seen = set()
while pq:
    tmp = heappop(pq)
    heat = tmp[0]
    r = tmp[1]
    c = tmp[2]
    dir = tmp[3]
    left = tmp[4]
    if (r, c) == (len(grid)-1, len(grid[0])-1) and left >= 4:
        print(heat)
        break
    if (r, c, dir, left) in seen:
        continue
    seen.add((r, c, dir, left))
    ndirs = []
    if left >= 4:
        ndirs.append((dir+1)%4)
        ndirs.append((dir+3)%4)
    if left <= 9: ndirs.append(dir)
    for ndir in ndirs:
        nr = r+drs[ndir]
        nc = c+dcs[ndir]
        nleft = left+1 if dir == ndir else 1
        if valid(nr, nc) and heat+grid[nr][nc] < minHeat[nr][nc][ndir][nleft]:
            minHeat[nr][nc][ndir][nleft] = heat+grid[nr][nc]
            heappush(pq, (heat+grid[nr][nc], nr, nc, ndir, nleft))

