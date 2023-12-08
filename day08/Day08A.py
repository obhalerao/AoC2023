lines = [l.strip() for l in open("../input.txt").readlines()]

instrs = lines[0]

mp = {}
for line in lines[2:]:
    l = line.split(" = ")
    key = l[0]
    val = l[1].split(", ")
    v2 = (val[0][1:], val[1][:-1])
    mp[key] = v2


cnt = 0
cur = "AAA"
while cur != "ZZZ":
    v = mp[cur]
    if instrs[cnt%len(instrs)] == "L":
        cur = v[0]
    else:
        cur = v[1]
    cnt+=1
print(cnt)