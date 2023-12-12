lines = [l.strip() for l in open("../input.txt").readlines()]

grid = [[i for i in j] for j in lines]
ngrid = []
for i in grid:
    ngrid.append(i)
    if all(j == '.' for j in i):
        ngrid.append(i)
grid = ngrid
ngrid = [[] for j in grid]
for j in range(len(grid[0])):
    yes = all(grid[i][j]=='.' for i in range(len(grid)))
    for i in range(len(grid)):
        ngrid[i].append(grid[i][j])
        if yes:
            ngrid[i].append(grid[i][j])

grid = ngrid
pts = []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '#':
            pts.append((i,j))
sm = 0
for i in range(len(pts)):
    for j in range(i+1, len(pts)):
        sm+=(abs(pts[i][0]-pts[j][0])+abs(pts[i][1]-pts[j][1]))

print(sm)