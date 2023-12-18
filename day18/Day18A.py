from shapely.geometry import Polygon

lines = [l.strip() for l in open("../input.txt").readlines()]

curr = (0, 0)
boundaries = []
for line in lines:
    l = line.split()
    ch = l[0]
    amt = int(l[1])
    for q in range(amt):
        boundaries.append(curr)
        if ch == 'R':
            curr = (curr[0], curr[1]+1)
        elif ch == 'L':
            curr = (curr[0], curr[1]-1)
        elif ch == 'U':
            curr = (curr[0]-1, curr[1])
        else:
            curr = (curr[0]+1, curr[1])

# pick's theorem again lmfao
area = Polygon(boundaries).area
num_pts = (area-(len(boundaries))//2+1)
print(num_pts+len(boundaries))

