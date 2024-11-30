import operator
lines = [l.strip() for l in open("../input.txt").readlines()]

stones = []

def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], -(a[0]*b[2]-a[2]*b[0]), a[0]*b[1]-a[1]*b[0])

def dot(a, b):
    return sum(i*j for i,j in zip(a,b))

def mul(a, b):
    return tuple(a*i for i in b)

def sub(a, b):
    return tuple(map(operator.sub, a, b))

def div(a, b):
    return tuple(map(operator.truediv, a, b))

def add(a, b):
    return tuple(map(operator.add, a, b))

for line in lines:
    w = line.split(" @ ")
    coords = [int(i) for i in w[0].split(", ")]
    vels = [int(i) for i in w[1].split(", ")]
    stones.append(((coords[0], coords[1], coords[2]), (vels[0], vels[1], vels[2])))

p1 = sub(stones[1][0], stones[0][0])
p2 = sub(stones[2][0], stones[0][0])
v1 = sub(stones[1][1], stones[0][1])
v2 = sub(stones[2][1], stones[0][1])

t1 = -1*dot(cross(p1, p2), v2)/(dot(cross(v1, p2), v2))
t2 = -1*dot(cross(p1, p2), v1)/(dot(cross(p1, v2), v1))

c1 = tuple(map(operator.add, stones[1][0], mul(t1, stones[1][1])))
c2 = tuple(map(operator.add, stones[2][0], mul(t2, stones[2][1])))

v = mul(1.0/(t2-t1), sub(c2, c1))
p = sub(c1, mul(t1, v))
print(sum((p[0], p[1], p[2])))