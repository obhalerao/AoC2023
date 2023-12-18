from collections import deque
lines = [l.strip() for l in open("../input.txt").readlines()]

grid = [[i for i in j] for j in lines]

drs = [0,1,0,-1]
dcs = [1,0,-1,0]

RIGHT=0
DOWN=1
LEFT=2
UP=3

def valid(r, c):
    global grid
    return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])

def solve(start):
    global grid,drs,dcs
    seen = set()

    q = deque()
    q.appendleft(start)
    while q:
        cur = q.popleft()
        if cur in seen:
            continue
        seen.add(cur)
        r = cur[0]
        c = cur[1]
        dir = cur[2]
        if grid[r][c] == '.':
            nr = r + drs[dir]
            nc = c + dcs[dir]
            ndir = dir
            if valid(nr, nc):
                q.append((nr, nc, ndir))
        elif grid[r][c] == '/':
            ndir = -1
            if dir == 0:
                ndir = 3
            if dir == 3:
                ndir = 0
            if dir == 1:
                ndir = 2
            if dir == 2:
                ndir = 1
            nr = r + drs[ndir]
            nc = c + dcs[ndir]
            if valid(nr, nc):
                q.append((nr, nc, ndir))
        elif grid[r][c] == '\\':
            ndir = -1
            if dir == 0:
                ndir = 1
            if dir == 1:
                ndir = 0
            if dir == 3:
                ndir = 2
            if dir == 2:
                ndir = 3
            nr = r + drs[ndir]
            nc = c + dcs[ndir]
            if valid(nr, nc):
                q.append((nr, nc, ndir))
        elif (grid[r][c] == '-' and dir % 2 == 0) or (grid[r][c] == '|' and dir % 2 == 1):
            nr = r + drs[dir]
            nc = c + dcs[dir]
            ndir = dir
            if valid(nr, nc):
                q.append((nr, nc, ndir))
        else:
            ndir1 = (dir + 1) % 4
            ndir2 = (dir + 3) % 4
            nr1 = r + drs[ndir1]
            nc1 = c + dcs[ndir1]
            if valid(nr1, nc1):
                q.append((nr1, nc1, ndir1))
            nr2 = r + drs[ndir2]
            nc2 = c + dcs[ndir2]
            if valid(nr2, nc2):
                q.append((nr2, nc2, ndir2))

    ns = set()
    for i in seen:
        ns.add((i[0], i[1]))

    return len(ns)



ans = 0
for i in range(len(grid)):
    ans = max(ans, solve((i, 0, RIGHT)))
    ans = max(ans, solve((i, len(grid[0])-1, LEFT)))

for i in range(len(grid[0])):
    ans = max(ans, solve((0, i, DOWN)))
    ans = max(ans, solve((len(grid)-1, i, UP)))
print(ans)
#(r, c, dir)

