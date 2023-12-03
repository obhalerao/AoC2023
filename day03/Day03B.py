lines = [l.strip() for l in open("../input.txt").readlines()]

dxs = [-1, 0, 1]
dys = [-1, 0, 1]

grid = [[i for i in line] for line in lines]
parts = [[None for i in line] for line in lines]
sm = 0
cnt = 0
for i in range(len(grid)):
    on = False
    cnum = 0
    start = -1
    good = False
    for j in range(len(grid[i])):
        c = grid[i][j]
        if c.isdigit():
            if not on: start = j
            on = True
            cnum*=10
            cnum+=int(c)
        else:
            on = False
            if good:
                for x in range(start, j):
                    parts[i][x] = (cnt, cnum)
                cnt += 1
            cnum = 0
            good = False

        if on:
            for dx in dxs:
                for dy in dys:
                    if dx != 0 or dy != 0:
                        nx = i+dx
                        ny = j+dy
                        if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[0]):
                            nc = grid[nx][ny]
                            if not nc.isdigit() and nc != '.':
                                good = True
    if good:
        for x in range(start, len(grid[i])):
            parts[i][x] = (cnt, cnum)
        cnt+=1

for i in range(len(grid)):
    for j in range(len(grid[i])):
        c = grid[i][j]
        if c != '*': continue
        st1 = {}
        for dx in dxs:
            for dy in dys:
                if dx != 0 or dy != 0:
                    nx = i + dx
                    ny = j + dy
                    if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[0]):
                        nc = parts[nx][ny]
                        if nc:
                            st1[nc[0]] = nc[1]
        if len(st1) == 2:
            p=1
            for elem in st1:
                p*=st1[elem]
            sm+=p


print(sm)