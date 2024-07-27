from scipy import interpolate
lines = [l.strip() for l in open("../input.txt").readlines()]
val = 202300
def count_pts(num_steps):
    global lines
    n = len(lines)
    m = len(lines[0])

    dxs = [0, 1, 0, -1]
    dys = [1, 0, -1, 0]
    coords = [set() for i in range(num_steps+1)]
    start = None
    for i, line in enumerate(lines):
        for j, ch in enumerate(line):
            if ch == 'S':
                start = (i, j)
                break

    coords[0].add(start)
    for iteri in range(num_steps):
        for x, y in coords[iteri]:
            for dx, dy in zip(dxs, dys):
                nx = x + dx
                ny = y + dy
                if lines[(nx+n)%n][(ny+m)%m] == '#':
                    continue
                coords[iteri + 1].add((nx, ny))
    return len(coords[num_steps])

a = count_pts(65)
b = count_pts(65+131)
c = count_pts(65+2*131)

print(a, b, c)

f = interpolate.interp1d([0, 1, 2], [a, b, c], kind="quadratic", fill_value="extrapolate")
print(f(val))