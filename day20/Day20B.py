from collections import deque
import math
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

final_layer = [m1 for m1 in edges if 'rx' in edges[m1]]

semi_final_layer = set(module for module in edges if final_layer[0] in edges[module])
cycle_lengths = []

buttonCnt = 0
while True:
    buttonCnt += 1
    q = deque()
    q.append(('broadcaster', 0, None)) # (node id, pulse, previous)
    good = False
    while q:
        tmp = q.popleft()
        nd = tmp[0]
        pulse = tmp[1]
        prev = tmp[2]
        if nd == 'rx' and pulse == 0:
            good = True
            break
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
            res = 1 if 0 in prevs[nd].values() else 0
            for e in edges[nd]:
                q.append((e, res, nd))
            if nd in semi_final_layer and res == 1:
                cycle_lengths.append(buttonCnt)
                semi_final_layer.remove(nd)

    if not semi_final_layer:
        break

print(math.lcm(*cycle_lengths))




