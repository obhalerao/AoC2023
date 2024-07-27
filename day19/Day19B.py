from collections import deque
lines = [l.strip() for l in open("../input.txt").readlines()]

def computeCnt(state):
    ans = 1
    for elem in state:
        ans*=(state[elem][1]-state[elem][0]+1)
    return ans


sm = 0

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

state = ({'x':(1, 4000),'m':(1,4000),'a':(1,4000),'s':(1,4000)},'in')
q = deque()
q.append(state)
while q:
    curr = q.popleft()
    if curr[1] == 'R':
        continue
    if curr[1] == 'A':
        sm+=computeCnt(curr[0])
        continue
    wfs = workflows[curr[1]]
    for residx, res in enumerate(wfs):
        if residx == len(wfs) - 1:
            nstate = ({i:curr[0][i] for i in curr[0]}, res)
            q.append(nstate)
            break
        cond, dest = res
        if cond[1] == '<':
            if curr[0][cond[0]][1] < cond[2]:
                nstate = ({i: curr[0][i] for i in curr[0]}, dest)
                q.append(nstate)
                break
            elif curr[0][cond[0]][0] < cond[2]:
                nstate1 = ({i: curr[0][i] for i in curr[0]}, dest)
                nstate2 = ({i: curr[0][i] for i in curr[0]}, curr[1])
                nstate1[0][cond[0]] = (curr[0][cond[0]][0], cond[2]-1)
                nstate2[0][cond[0]] = (cond[2], curr[0][cond[0]][1])
                q.append(nstate1)
                curr = nstate2
        elif cond[1] == '>':
            if curr[0][cond[0]][0] > cond[2]:
                nstate = ({i: curr[0][i] for i in curr[0]}, dest)
                q.append(nstate)
                break
            elif curr[0][cond[0]][1] > cond[2]:
                nstate1 = ({i: curr[0][i] for i in curr[0]}, curr[1])
                nstate2 = ({i: curr[0][i] for i in curr[0]}, dest)
                nstate1[0][cond[0]] = (curr[0][cond[0]][0], cond[2])
                nstate2[0][cond[0]] = (cond[2] + 1, curr[0][cond[0]][1])
                q.append(nstate2)
                curr = nstate1
print(sm)



