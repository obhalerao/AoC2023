lines = [l.strip() for l in open("../input.txt").readlines()]

dxs = [-1, 0, 1]
dys = [-1, 0, 1]

grid = lines
sm = 0
for i in range(len(grid)):
    on = False
    cnum = 0
    good = False
    for j in range(len(grid[i])):
        c = grid[i][j]
        if c.isdigit():
            on = True
            cnum*=10
            cnum+=int(c)
        else:
            on = False
            if good:
                sm+=cnum
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
        sm+=cnum


print(sm)