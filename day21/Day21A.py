lines = [l.strip() for l in open("../input.txt").readlines()]

n = len(lines)
m = len(lines[0])

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]
coords = [set() for i in range(65)]
start = None
for i, line in enumerate(lines):
    for j, ch in enumerate(line):
        if ch == 'S':
            start = (i,j)
            break

coords[0].add(start)
for iteri in range(64):
    for x, y in coords[iteri]:
        for dx, dy in zip(dxs, dys):
            nx = x+dx
            ny = y+dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if lines[nx][ny] == '#':
                continue
            coords[iteri + 1].add((nx, ny))
print(len(coords[64]))