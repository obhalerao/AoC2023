lines = [l.strip() for l in open("../input.txt").readlines()]

sm = 0

digits = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}

for line in lines:
    d1 = 0
    d2 = 0
    for i in range(len(line)):
        if line[i].isdigit():
            d1 = int(line[i])
            break
        if i < len(line)+3 and line[i:i+3] in digits:
            d1 = digits[line[i:i+3]]
            break
        if i < len(line)+4 and line[i:i+4] in digits:
            d1 = digits[line[i:i+4]]
            break
        if i < len(line)+5 and line[i:i+5] in digits:
            d1 = digits[line[i:i+5]]
            break

    for i in range(len(line)-1, -1, -1):
        if line[i].isdigit():
            d2 = int(line[i])
            break
        if i < len(line)+3 and line[i:i+3] in digits:
            d2 = digits[line[i:i+3]]
            break
        if i < len(line)+4 and line[i:i+4] in digits:
            d2 = digits[line[i:i+4]]
            break
        if i < len(line)+5 and line[i:i+5] in digits:
            d2 = digits[line[i:i+5]]
            break

    sm+=(10*d1+d2)
print(sm)