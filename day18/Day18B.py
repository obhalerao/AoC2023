from shapely.geometry import Polygon

lines = [l.strip() for l in open("../input.txt").readlines()]

curr = (0, 0)
boundaries = []
boundaryCnt = 0
for line in lines:
    l = line.split()
    encoding = l[2]
    ch = None
    if encoding[-2] == '0':
        ch = 'R'
    elif encoding[-2] == '1':
        ch = 'D'
    elif encoding[-2] == '2':
        ch = 'L'
    else:
        ch = 'U'
    amt = int(encoding[2:-2], 16)
    boundaries.append(curr)
    boundaryCnt += amt
    if ch == 'R':
        curr = (curr[0], curr[1]+amt)
    elif ch == 'L':
        curr = (curr[0], curr[1]-amt)
    elif ch == 'U':
        curr = (curr[0]-amt, curr[1])
    else:
        curr = (curr[0]+amt, curr[1])

# pick's theorem again lmfao
area = Polygon(boundaries).area
num_pts = (area-(boundaryCnt)//2+1)
print(num_pts+boundaryCnt)

