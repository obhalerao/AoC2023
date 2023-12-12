lines = [l.strip() for l in open("../input.txt").readlines()]

strr = None
sm = 0
cnt = 0
def test(lst):
    global strr
    st = strr
    idx = 0
    on = False
    cc = 0
    for i in range(len(st)):
        if not on and st[i] == '#':
            on = True
            cc = 1
        elif on and st[i] == '.':
            on = False
            if idx >= len(lst) or cc != lst[idx]:
                return False
            idx+=1
        elif st[i] == '#':
            cc+=1
    if on:
        if idx >= len(lst) or cc != lst[idx]:
            return False
        else:
            idx+=1
    return idx == len(lst)

def bf(idx, lst):
    global strr, sm, cnt
    if idx == len(strr):
        if test(lst):
            cnt+=1
        return
    if strr[idx] == '?':
        strr[idx] = '.'
        bf(idx+1, lst)
        strr[idx] = '#'
        bf(idx+1, lst)
        strr[idx] = '?'
    else:
        bf(idx+1, lst)



for idx, line in enumerate(lines):
    l = line.split()
    cnt = 0
    strr = [i for i in l[0]]
    v = [int(i) for i in l[1].split(',')]
    bf(0, v)
    sm+=cnt
print(sm)
