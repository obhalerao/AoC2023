lines = [l.strip() for l in open("../input.txt").readlines()]

sm = 0
for ln in lines:
    l = list(reversed([int(i) for i in ln.split()]))
    vals = [l]
    good = False
    while not good:
        good = True
        cl = vals[-1]
        nl = []
        for i in range(len(cl)-1):
            nl.append(cl[i+1]-cl[i])
            if nl[-1] != 0:
                good = False
        vals.append(nl)
    for i in range(len(vals)-1, -1, -1):
        if i == len(vals)-1:
            vals[i].append(0)
        else:
            vals[i].append(vals[i][-1]+vals[i+1][-1])
    sm+=vals[0][-1]
print(sm)