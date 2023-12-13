lines = [l.strip() for l in open("../input.txt").readlines()]

def reflects(grid, oval):
    n = len(grid)
    m = len(grid[0])
    for i in range(n-1):
        ni = n-i
        good = True
        for j in range(min(i+1, ni-1)):
            i1 = i-j
            i2 = (i+1)+j
            if not all(grid[i1][jj]==grid[i2][jj] for jj in range(m)):
                good = False
                break
        if good and (100)*(i+1) != oval:
            return (100)*(i+1)
    for i in range(m-1):
        ni = m-i
        good = True
        for j in range(min(i+1, ni-1)):
            i1 = i-j
            i2 = (i+1)+j
            if not all(grid[jj][i1]==grid[jj][i2] for jj in range(n)):
                good = False
                break
        if good and i+1 != oval:
            return (i+1)
    return -1

sm = 0
grids = []
cgrid = []
for line in lines:
    if len(line) == 0:
        grids.append(cgrid)
        cgrid = []
    else:
        cgrid.append([i for i in line])
grids.append(cgrid)
for grid in grids:
    oval = reflects(grid, -529876)
    for i in range(len(grid)):
        broken = False
        for j in range(len(grid[0])):
            if grid[i][j] == '.':
                grid[i][j] = '#'
            else:
                grid[i][j] = '.'
            val = reflects(grid, oval)
            if val > 0:
                sm+=val
                broken = True
                break
            if grid[i][j] == '.':
                grid[i][j] = '#'
            else:
                grid[i][j] = '.'
        if broken:
            break

print(sm)

