# 이것도 dp 인듯
import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * (n + 1)

if n >= 1:
    dp[1] = 1
if n >= 2:
    dp[2] = 2
#  규칙성 : dp[k]= dp[k-1] + dp[k-2]

# range(start, end) 는 start ≤ i < end 인 값만 만든다
for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

print(dp[n])
