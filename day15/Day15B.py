lines = [l.strip() for l in open("../input.txt").readlines()]
line = lines[0].split(',')
sm = 0
boxes = [[] for i in range(256)]
for l in line:
    tmp = 0
    if '=' in l:
        k = l.split('=')
        val = int(k[1])
        id = k[0]
        for c in id:
            tmp += ord(c)
            tmp *= 17
            tmp %= 256
        good = False
        for idx in range(len(boxes[tmp])):
            if boxes[tmp][idx][0] == id:
                boxes[tmp][idx] = (id, val)
                good = True
                break
        if not good:
            boxes[tmp].append((id, val))
    else:
        id = l[:-1]
        for c in id:
            tmp += ord(c)
            tmp *= 17
            tmp %= 256
        for idx in range(len(boxes[tmp])):
            if boxes[tmp][idx][0] == id:
                del boxes[tmp][idx]
                break

for idx1, box in enumerate(boxes):
    for idx, l in enumerate(box):
        sm+=((idx1+1)*(idx+1)*l[1])

print(sm)