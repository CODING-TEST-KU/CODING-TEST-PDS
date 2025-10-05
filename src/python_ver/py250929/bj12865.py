n, k = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(n)]

# dp[c] 용량 c에서 얻을 수 있는 최대 가치
dp = [0] * (k + 1)

for w, v in items:
    for c in range(k, w - 1, -1):
        dp[c] = max(dp[c], dp[c - w] + v)
print(dp[k])
