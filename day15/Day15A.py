lines = [l.strip() for l in open("../input.txt").readlines()]
line = lines[0].split(',')
sm = 0
for l in line:
    tmp = 0
    for c in l:
        tmp+=ord(c)
        tmp*=17
        tmp%=256
    sm+=tmp
print(sm)