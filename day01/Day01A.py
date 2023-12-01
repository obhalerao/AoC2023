lines = [l.strip() for l in open("../input.txt").readlines()]

sm = 0
for line in lines:
    d1 = 0
    d2 = 0
    for i in range(len(line)):
        if line[i].isdigit():
            d1 = int(line[i])
            break
    for i in range(len(line)-1, -1, -1):
        if line[i].isdigit():
            d2 = int(line[i])
            break
    sm+=(10*d1+d2)
print(sm)