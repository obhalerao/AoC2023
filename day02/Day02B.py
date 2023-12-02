lines = [l.strip() for l in open("../input.txt").readlines()]
idx = 1
sm=0
for line in lines:
    l = line.split(':')[1].strip()
    l2 = l.split('; ')
    good = True
    cnts = {'red':0, 'blue':0,'green':0}
    for l3 in l2:
        l4 = l3.split(', ')
        cnt = {}
        for l5 in l4:
            l6 = l5.split(' ')
            num = int(l6[0])
            col = l6[1]
            cnts[col] = max(cnts[col], num)
    p = 1
    for cnt in cnts:
        if cnts[cnt] == float("inf"):
            p *= 0
        else:
            p*=cnts[cnt]
    sm+=p
print(sm)