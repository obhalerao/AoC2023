def intersection(i1, i2):
    if i2[0] < i1[0]:
        i1, i2 = i2, i1
    if i1[1] < i2[0]:
        return None
    else:
        return (max(i1[0], i2[0]), min(i1[1], i2[1]))

def minus(i1, i2):
    result = []
    if i1[0] != i2[0]:
        result.append((i1[0], i2[0]-1))
    if i1[1] != i2[1]:
        result.append((i2[1]+1, i1[1]))
    return result



lines = [l.strip() for l in open("../input.txt").readlines()]

oseeds = [int(i) for i in lines[0].split(':')[1].split()]

seeds = [(oseeds[i], oseeds[i]+oseeds[i+1]-1) for i in range(0, len(oseeds), 2)]

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
    cur_range = [seed]
    for mp in maps:
        new_ranges = []
        for entry in mp:
            new_old_ranges = []
            for interval in cur_range:
                intersect = intersection(interval, (entry[1], entry[1]+entry[2]-1))
                if intersect != None:
                    new_ranges.append((intersect[0]+(entry[0]-entry[1]), intersect[1]+(entry[0]-entry[1])))
                    for i in minus(interval, intersect):
                        new_old_ranges.append(i)
                else:
                    new_old_ranges.append(interval)
                cur_range = new_old_ranges
        cur_range = cur_range + new_ranges
    cmin = min(cmin, min(i[0] for i in cur_range))
print(cmin)