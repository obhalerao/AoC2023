lines = [l.strip() for l in open("../input.txt").readlines()]
sm=0
for line in lines:
    l = line.split(':')[1]
    ll = l.split('|')
    cn = {int(i) for i in ll[0].split()}
    yn = [int(i) for i in ll[1].split()]
    tmp=1
    for num in yn:
        if num in cn:
            tmp*=2
    sm+=(tmp//2)
print(sm)