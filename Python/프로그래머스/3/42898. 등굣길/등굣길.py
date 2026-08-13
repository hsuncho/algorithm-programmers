def solution(m, n, puddles):
    MOD = 1000000007
    # 가로 m 세로 n
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for px, py in puddles:
        dp[px][py] = -1
    
    dp[1][1] = 1
    
    for x in range(1, m + 1):
        for y in range(1, n + 1):
            if dp[x][y] == -1:
                dp[x][y] = 0
                continue
            if x == 1 and y == 1:
                continue
            dp[x][y] = (dp[x-1][y] + dp[x][y-1]) % MOD    
    return dp[m][n]