lines = [l.strip() for l in open("../input.txt").readlines()]
cnts = [1 for i in range(len(lines))]
sm = 0
for idx,line in enumerate(lines):
    sm+=cnts[idx]
    l = line.split(':')[1]
    ll = l.split('|')
    cn = {int(i) for i in ll[0].split()}
    yn = [int(i) for i in ll[1].split()]
    tmp=0
    for num in yn:
        if num in cn:
            tmp+=1
    for i in range(tmp):
        cnts[idx+i+1]+=cnts[idx]
print(sm)