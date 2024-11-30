import operator
lines = [l.strip() for l in open("../input.txt").readlines()]

SQ_LEFT = 200000000000000
SQ_RIGHT = 400000000000000

def intersection(a, b, c, d):
    # Line AB represented as a1x + b1y = c1
    a1 = b[1]-a[1]
    b1 = a[0]-b[0]
    c1 = a1*(a[0]) + b1*(a[1])

    # Line CD represented as a2x + b2y = c2
    a2 = d[1]-c[1]
    b2 = c[0]-d[0]
    c2 = a2*(c[0]) + b2*(c[1])

    determinant = a1*b2 - a2*b1

    if(determinant == 0):
        return None
    else:
        x = (b2*c1 - b1*c2)/determinant
        y = (a1*c2 - a2*c1)/determinant
        return (x, y)

stones = []

for line in lines:
    w = line.split(" @ ")
    coords = [int(i) for i in w[0].split(", ")]
    vels = [int(i) for i in w[1].split(", ")]
    stones.append(((coords[0], coords[1]), (vels[0], vels[1])))

intcnt = 0
for i in range(len(stones)):
    for j in range(i+1, len(stones)):
        pt1 = stones[i][0]
        pt2 = tuple(map(operator.add, stones[i][0], stones[i][1]))
        pt3 = stones[j][0]
        pt4 = tuple(map(operator.add, stones[j][0], stones[j][1]))
        intpt = intersection(pt1, pt2, pt3, pt4)
        if intpt is None:
            continue
        if not (SQ_LEFT <= intpt[0] <= SQ_RIGHT and SQ_LEFT <= intpt[1] <= SQ_RIGHT):
            continue
        diff1 = intpt[0] - stones[i][0][0]
        diff2 = intpt[0] - stones[j][0][0]
        if diff1*stones[i][1][0] >= 0 and diff2*stones[j][1][0] >= 0:
            intcnt+=1
print(intcnt)