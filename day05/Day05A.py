lines = [l.strip() for l in open("../input.txt").readlines()]

seeds = [int(i) for i in lines[0].split(':')[1].split()]

maps = []

cmap = []
for line in lines[1:]:
    if len(line) == 0:
        if cmap != []:
            maps.append(cmap)
        continue
    if line.endswith(':'):
        cmap = []
        continue
    cmap.append(tuple(int(i) for i in line.split()))

maps.append(cmap)

cmin = float("inf")

for seed in seeds:
    cnum = seed
    for mp in maps:
        for entry in mp:
            if entry[1] <= cnum and entry[1]+entry[2] > cnum:
                cnum = entry[0]+(cnum-entry[1])
                break
    cmin = min(cnum, cmin)

print(cmin)