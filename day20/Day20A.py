from collections import deque
lines = [l.strip() for l in open("../input.txt").readlines()]

types = {}
edges = {}
prevs = {}
flipstates = {}

for line in lines:
    l = line.split(' -> ')
    name = l[0]
    if name[0] == '%' or name[0] == '&':
        types[name[1:]] = name[0]
        if name[0] == '%':
            flipstates[name[1:]] = 0
        name = name[1:]
    edges[name] = []
    for dest in l[1].split(', '):
        edges[name].append(dest)
        if dest not in prevs:
            prevs[dest] = {}
        prevs[dest][name] = 0

pulses = [0,0]
for x in range(1000):
    q = deque()
    q.append(('broadcaster', 0, None)) # (node id, pulse, previous)
    while q:
        tmp = q.popleft()
        nd = tmp[0]
        pulse = tmp[1]
        prev = tmp[2]
        pulses[pulse]+=1
        if nd == 'broadcaster':
            for e in edges[nd]:
                q.append((e, pulse, nd))
        elif nd in types and types[nd] == '%':
            if pulse == 0:
                flipstates[nd] = 1-flipstates[nd]
                for e in edges[nd]:
                    q.append((e, flipstates[nd], nd))
        elif nd in types and types[nd] == '&':
            prevs[nd][prev] = pulse
            res = int(all(prevs[nd][i] == 1 for i in prevs[nd]))
            for e in edges[nd]:
                q.append((e, 1-res, nd))
print(pulses[0]*pulses[1])




