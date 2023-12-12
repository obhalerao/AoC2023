lines = [l.strip() for l in open("../input.txt").readlines()]

grid = [[i for i in j] for j in lines]
rows = [[False for i in j] for j in lines]
cols = [[False for i in j] for j in lines]

DIST = 1000000

ngrid = []
for idx, i in enumerate(grid):
    ngrid.append(i)
    if all(j == '.' for j in i):
        rows[idx] = [True for j in i]

grid = ngrid
ngrid = [[] for j in grid]
for j in range(len(grid[0])):
    yes = all(grid[i][j]=='.' for i in range(len(grid)))
    for i in range(len(grid)):
        ngrid[i].append(grid[i][j])
        if yes:
            cols[i][j] = True

grid = ngrid
pts = []
ci = 0
for i in range(len(grid)):
    cj = 0
    for j in range(len(grid[0])):
        if grid[i][j] == '#':
            pts.append((ci,cj))
        if cols[i][j]:
            cj+=DIST
        else:
            cj+=1
    if rows[i][0]:
        ci+=DIST
    else:
        ci+=1
sm = 0
for i in range(len(pts)):
    for j in range(i+1, len(pts)):
        sm+=(abs(pts[i][0]-pts[j][0])+abs(pts[i][1]-pts[j][1]))

print(sm)