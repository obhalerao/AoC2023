lines = [l.strip() for l in open("../input.txt").readlines()]
idx = 1
sm=0
for line in lines:
    l = line.split(':')[1].strip()
    l2 = l.split('; ')
    good = True
    for l3 in l2:
        l4 = l3.split(', ')
        cnt = {}
        for l5 in l4:
            l6 = l5.split(' ')
            num = int(l6[0])
            col = l6[1]
            cnt[col] = num
        if not (('red' not in cnt or cnt['red'] <= 12) and ('green' not in cnt or cnt['green'] <= 13) and ('blue' not in cnt or cnt['blue'] <= 14)):
            good = False
            break
    if good:
        sm+=idx
    idx+=1
print(sm)