from collections import Counter
from functools import cmp_to_key
lines = [l.strip() for l in open("../input.txt").readlines()]



def typ(hand):
    counter = Counter(hand)
    jcnt = counter['J']
    del counter['J']
    lst = counter.most_common()
    if len(lst) <= 1:
        return 7
    if lst[0][1]+jcnt == 5:
        return 7
    elif lst[0][1]+jcnt == 4:
        return 6
    elif (lst[0][1]+jcnt == 3 and lst[1][1] == 2) or (lst[0][1] == 3 and lst[1][1]+jcnt == 2):
        return 5
    elif lst[0][1]+jcnt == 3:
        return 4
    elif (lst[0][1]+jcnt == 2 and lst[1][1] == 2) or (lst[0][1] == 2 and lst[1][1]+jcnt == 2):
        return 3
    elif lst[0][1]+jcnt == 2:
        return 2
    return 1

def cmp(h1, h2):
    ordering = {'J':0,'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'T':9,'Q':11,'K':12,'A':13}
    h1 = h1[0]
    h2 = h2[0]
    t1 = typ(h1)
    t2 = typ(h2)
    if t1 != t2:
        if t1 < t2:
            return -1
        else:
            return 1
    else:
        for i in range(5):
            if ordering[h1[i]] < ordering[h2[i]]:
                return -1
            elif ordering[h1[i]] > ordering[h2[i]]:
                return 1
    return 0


hands = []
for line in lines:
    l = line.split()
    hands.append((l[0], int(l[1])))
hands.sort(key=cmp_to_key(cmp))
ans=0
for i in range(len(hands)):
    ans+=(i+1)*(hands[i][1])
print(ans)