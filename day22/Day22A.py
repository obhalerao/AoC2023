from operator import itemgetter
lines = [l.strip() for l in open("../input.txt").readlines()]

grid = [[[-1 for z in range(350)] for y in range(10)] for x in range(10)]

pos = {}

def fall(brick):
    global grid, pos
    nlist = []
    for elem in pos[brick]:
        if elem[2] == 1 or (grid[elem[0]][elem[1]][elem[2]-1] != -1 and grid[elem[0]][elem[1]][elem[2]-1] != brick):
            return False
        nlist.append((elem[0], elem[1], elem[2]-1))
    for elem in pos[brick]:
        grid[elem[0]][elem[1]][elem[2]] = -1
    for elem in nlist:
        grid[elem[0]][elem[1]][elem[2]] = brick
    pos[brick] = nlist
    return True

for idx, line in enumerate(lines):
    m = line.split("~")
    ss = m[0]
    ee = m[1]
    start = [int(i) for i in ss.split(',')]
    end = [int(i) for i in ee.split(',')]
    pos[idx] = []
    for x in range(start[0], end[0]+1):
        for y in range(start[1], end[1]+1):
            for z in range(start[2], end[2]+1):
                grid[x][y][z] = idx
                pos[idx].append((x, y, z))
    pos[idx].sort(key=itemgetter(2))

# blocks fall down
good = False
while not good:
    good = True
    done = set()
    for z in range(2, 350):
        for x in range(10):
            for y in range(10):
                if grid[x][y][z] == -1 or grid[x][y][z] in done:
                    continue
                cur = grid[x][y][z]
                result = fall(grid[x][y][z])
                if result:
                    good = False
                done.add(cur)

supports = {}
for brick in pos:
    supports[brick] = set()
    for elem in pos[brick]:
        if elem[2] != 1 and grid[elem[0]][elem[1]][elem[2]-1] != -1 and grid[elem[0]][elem[1]][elem[2]-1] != brick:
            supports[brick].add(grid[elem[0]][elem[1]][elem[2]-1])

no = set()
for brick in supports:
    if len(supports[brick]) == 1:
        no.add(list(supports[brick])[0])

print(len(pos)-len(no))