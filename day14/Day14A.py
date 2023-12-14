lines = [l.strip() for l in open("../input.txt").readlines()]

grid = [[i for i in j] for j in lines]
for i in range(len(grid)):
    for j in range(len(grid[0])):
        ci = i
        if grid[i][j] == 'O':
            while ci > 0 and grid[ci-1][j] == '.':
                grid[ci][j] = '.'
                ci-=1
                grid[ci][j] = 'O'

sm = 0
for j in range(len(grid[0])):
    for i in range(len(grid)):
        if grid[i][j] == 'O':
            sm+=(len(grid)-i)

print(sm)