lines = [l.strip() for l in open("../input.txt").readlines()]

times = []
dists = []
l1 = lines[0].split()
l2 = lines[1].split()
for i in l1[1:]:
    times.append(i.strip())
for i in l2[1:]:
    dists.append(i.strip())

time = int(''.join(times))
dist = int(''.join(dists))

lo = -1
hi = time

while lo + 1 < hi:
    mid = (lo+hi)//2
    val = (mid)*(time-mid)
    if val > dist:
        hi = mid
    else:
        lo = mid

ans1 = hi

lo = 0
hi = time+1
while lo + 1 < hi:
    mid = (lo+hi)//2
    val = (mid)*(time-mid)
    if val > dist:
        lo = mid
    else:
        hi = mid

ans2 = lo
print(ans2-ans1+1)