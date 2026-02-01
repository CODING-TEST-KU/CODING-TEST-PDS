n = int(input())
dp = [0] * 1001

# dp[n]은 2*n크기의 직사각형을 1*2,2*1 타일로 채우는 방법의 수
if n > 0:
    dp[1] = 1
if n > 1:
    dp[2] = 2
if n > 2:
    dp[3] = 3

for i in range(4, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n]%10007)
