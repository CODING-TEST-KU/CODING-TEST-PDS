import sys

input = sys.stdin.readline

n = int(input())
tri = []

for _ in range(n):
    tri.append(list(map(int, input().split())))

# 해당 지점까지 오는 길 중 가장 비용이 큰 경우 dp

# dp = tri
dp = [row[:] for row in tri]

for i in range(1, n):
    for j in range(i + 1):
        # 아래에서 위를 찾을 때는 현재 j는 위의 j에서 왔거나 위의 j-1에서 왔다
        if j == 0:
            dp[i][j] = dp[i - 1][j] + tri[i][j]
        elif j == i:
            dp[i][j] = dp[i - 1][j - 1] + tri[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + tri[i][j]

print(max(dp[n - 1]))