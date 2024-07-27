lines = [l.strip() for l in open("../input.txt").readlines()]

workflows = {}
lineidx = 0
while len(lines[lineidx]) > 0:
    l1 = lines[lineidx].split('{')
    wf = l1[0]
    l2 = l1[1][:-1].split(',')
    reslst = []
    for l3 in l2:
        if ':' not in l3:
            reslst.append(l3)
            break
        l4 = l3.split(':')
        l5 = l4[0]
        if '<' in l5:
            cond = (l5.split('<')[0],'<',int(l5.split('<')[1]))
        else:
            cond = (l5.split('>')[0],'>',int(l5.split('>')[1]))
        dest = l4[1]
        reslst.append((cond, dest))
    workflows[wf] = reslst
    lineidx+=1

lineidx+=1
sm = 0
while lineidx < len(lines):
    cmap = {}
    l1 = lines[lineidx][1:-1].split(',')
    for l2 in l1:
        l3 = l2.split('=')
        cmap[l3[0]] = int(l3[1])
    cur = 'in'
    while True:
        for residx, res in enumerate(workflows[cur]):
            if residx == len(workflows[cur])-1:
                cur = res
                break
            cond, dest = res
            if cond[1] == '<':
                if cmap[cond[0]] < cond[2]:
                    cur = dest
                    break
            elif cond[1] == '>':
                if cmap[cond[0]] > cond[2]:
                    cur = dest
                    break
        if cur == 'A' or cur == 'R':
            if cur == 'A':
                for elem in cmap:
                    sm+=cmap[elem]
            break
    lineidx+=1
print(sm)

