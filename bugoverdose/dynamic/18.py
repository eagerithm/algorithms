# 앱 (https://www.acmicpc.net/problem/7579)

# 현재 활성화 되어 있는 앱 A1, ..., AN 중에서 몇 개를 비활성화 하여 M 바이트 이상의 메모리를 추가로 확보
# 비활성화 했을 경우의 비용 ci의 합을 최소화하여 필요한 메모리 M 바이트를 확보하는 방법 찾기
# 단, 1 ≤ N ≤ 100, 1 ≤ M ≤ 10,000,000이며, 1 ≤ m1, ..., mN ≤ 10,000,000을 만족한다. 
# 또한, 0 ≤ c1, ..., cN ≤ 100이고, M ≤ m1 + m2 + ... + mN이다.

# 0-1 배낭문제(0-1 Knapsack Problem) : 담을 수 있는 물건이 나누어지지 않음(담는다 or 안담는다)

# 나의 정답
N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))
max_cost = sum(cost)

# dp[i][j] : i번째 앱까지 j의 비용으로 확보할 수 있는 최대 바이트 수
dp = [[0]*(max_cost+1) for _ in range(N+1)] # 중복 방지 목적으로 2차원 배열 필요

for i in range(N):
    m = memory[i]
    c = cost[i]
    
    for j in range(c): # idx = 0 ~ c-1까지는 그대로 사용
        dp[i+1][j] = dp[i][j]

    dp[i+1][c] = max(dp[i][c], dp[i][0] + m) # idx = c - 현재 앱 사용하도록 갱신

    for j in range(c+1, max_cost+1): # idx = c+1 ~ max_cost까지 갱신
        if dp[i][j-c] != 0: 
            dp[i+1][j] = max(dp[i][j], dp[i][j-c] + m) # 그대로 사용 vs 현재 앱 사용하도록 갱신
        else:
            dp[i+1][j] = dp[i][j] # 이전 단계가 없으면 그대로 사용
            
for idx in range(max_cost+1):
    if dp[N][idx] >= M:
        print(idx)
        break

# print(dp)
# [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
# [0, 0, 0, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
# [10, 0, 0, 40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
# [10, 0, 0, 40, 0, 0, 60, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
# [10, 0, 0, 40, 0, 45, 60, 0, 75, 0, 0, 95, 0, 0, 0, 0], 
# [10, 0, 0, 40, 50, 45, 60, 80, 75, 85, 100, 95, 115, 0, 0, 135]]
# ==================================================================
# 5 60
# 30 10 20 35 40
# 3 0 3 5 4

# 6

#  0  1  2  3  4  5  6 : 최대 비용
#  0  0  0  0  0  0  0 : 현재 상태
#  0  0  0 30  0  0  0 : (30, 3)
# 10  0  0 40  0  0  0 : (10, 0)
# 10  0  0 40  0  0 60 : (20, 3)
# 10  0  0 40  0 45 60 : (35, 5)
# 10  0  0 40 50 45 60 : (40, 4)
# ==================================================================