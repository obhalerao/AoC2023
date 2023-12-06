lines = [l.strip() for l in open("../input.txt").readlines()]

times = []
dists = []
l1 = lines[0].split()
l2 = lines[1].split()
for i in l1[1:]:
    times.append(int(i.strip()))
for i in l2[1:]:
    dists.append(int(i.strip()))

pd = 1
for i in range(len(times)):
    cnt = 0
    for j in range(times[i]):
        dist = (j*(times[i]-j))
        if dist > dists[i]:
            cnt+=1
    pd*=cnt
print(pd)