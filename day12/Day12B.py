lines = [l.strip() for l in open("../input.txt").readlines()]

strr = None
sm = 0
cnt = 0

for idx, line in enumerate(lines):
    l = line.split()
    cnt = 0
    strr = (([i for i in l[0]]+["?"])*5)
    strr[-1] = '.'
    v = [int(i) for i in l[1].split(',')]*5
    n = len(strr)
    m = len(v)
    dp = [[[0 for k in range(m+1)] for j in range(n+1)] for i in range(n+1)]
    dp[0][0][0] = 1
    for i in range(n):
        curcell = strr[i]
        for j in range(n+1):
            for k in range(m+1):
                if curcell == '.':
                    if j != 0:
                        if k != m and j == v[k]:
                            dp[i+1][0][k+1]+=dp[i][j][k]
                    else:
                        dp[i+1][0][k]+=dp[i][j][k]
                if curcell == '#' and j != n:
                    dp[i+1][j+1][k]+=dp[i][j][k]
                if curcell == '?':
                    if j != 0:
                        if k != m and j == v[k]:
                            dp[i + 1][0][k + 1] += dp[i][j][k]
                    else:
                        dp[i + 1][0][k] += dp[i][j][k]
                    if j != n:
                        dp[i + 1][j + 1][k] += dp[i][j][k]
    ans = sum(dp[n][l][m] for l in range(n+1))
    sm+=ans
print(sm)
