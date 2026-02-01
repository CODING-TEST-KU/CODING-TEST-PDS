n = int(input())

stair = [0]
dp = [0] * (n + 1)

for _ in range(n):
    stair.append(int(input()))

if n > 0:
    dp[1] = stair[1]
if n > 1:
    dp[2] = stair[1] + stair[2]
if n > 2:
    dp[3] = stair[3] + max(stair[1], stair[2])

for i in range(4, n + 1):
    dp[i] = stair[i] + max(dp[i - 2], stair[i - 1] + dp[i - 3])

print(dp[n])
