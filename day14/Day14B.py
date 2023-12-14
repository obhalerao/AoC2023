lines = [l.strip() for l in open("../input.txt").readlines()]

grid = [[i for i in j] for j in lines]

gmap = {}

ITERS = 1000000000
def cycle():
    global grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            ci = i
            if grid[i][j] == 'O':
                while ci > 0 and grid[ci-1][j] == '.':
                    grid[ci][j] = '.'
                    ci-=1
                    grid[ci][j] = 'O'
    for j in range(len(grid[0])):
        for i in range(len(grid)):
            cj = j
            if grid[i][j] == 'O':
                while cj > 0 and grid[i][cj-1] == '.':
                    grid[i][cj] = '.'
                    cj-=1
                    grid[i][cj] = 'O'
    for i in reversed(range(len(grid))):
        for j in range(len(grid[0])):
            ci = i
            if grid[i][j] == 'O':
                while ci < len(grid)-1 and grid[ci+1][j] == '.':
                    grid[ci][j] = '.'
                    ci+=1
                    grid[ci][j] = 'O'
    for j in reversed(range(len(grid[0]))):
        for i in range(len(grid)):
            cj = j
            if grid[i][j] == 'O':
                while cj < len(grid[0])-1 and grid[i][cj+1] == '.':
                    grid[i][cj] = '.'
                    cj+=1
                    grid[i][cj] = 'O'

sm = 0

ngrid = [[i for i in j] for j in grid]
cnt = 0
res = -1
gmap[tuple(tuple(i for i in j) for j in ngrid)] = cnt
while True:
    cycle()
    cnt+=1
    if tuple(tuple(i for i in j) for j in grid) in gmap:
        res = gmap[tuple(tuple(i for i in j) for j in grid)]
        break
    ngrid = [[i for i in j] for j in grid]
    gmap[tuple(tuple(i for i in j) for j in ngrid)] = cnt

rem = (ITERS-cnt)%(cnt-res)
for j in range(rem):
    cycle()

for j in range(len(grid[0])):
    for i in range(len(grid)):
        if grid[i][j] == 'O':
            sm+=(len(grid)-i)

print(sm)