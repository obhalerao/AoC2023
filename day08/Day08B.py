from math import gcd

lines = [l.strip() for l in open("../input.txt").readlines()]

def win(lst):
    for i in lst:
        if i[-1] != 'Z':
            return False
    return True

def win2(elem):
    return elem[-1] == 'Z'

instrs = lines[0]

mp = {}
for line in lines[2:]:
    l = line.split(" = ")
    key = l[0]
    val = l[1].split(", ")
    v2 = (val[0][1:], val[1][:-1])
    mp[key] = v2


cur = []
finans = -1
for k in mp:
    if k[-1] == 'A':
        cur.append(k)
for idx, elem in enumerate(cur):
    elem2 = elem
    cnt = 0

    while not win2(elem2):
        v = mp[elem2]
        if instrs[cnt%len(instrs)] == "L":
            elem2 = v[0]
        else:
            elem2 = v[1]
        cnt+=1
    if finans == -1:
        finans = cnt
    else:
        g = gcd(finans, cnt)
        finans = (finans*cnt)//g
print(finans)