import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
x = list(map(int, input().split()))

max_gap = 0

# 첫번째 가로등까지의 거리
max_gap = x[0] * 2

# 마지막 가로등에서 길의 끝까지의 거리
max_gap = max(max_gap, (n - x[-1]) * 2)

for i in range(len(x) - 1):
    gap = x[i + 1] - x[i]
    if gap % 2 == 1:
        gap += 1
    max_gap = max(max_gap, gap)

print(int(max_gap/2))