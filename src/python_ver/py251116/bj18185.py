# 그리디
import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

cost = 0

for i in range(n - 2):
    three = min(a[i], a[i + 1], a[i + 2])
    if three > 0:
        cost += three * 7
        a[i], a[i + 1], a[i + 2] = a[i] - three, a[i + 1] - three, a[i + 2] - three

for i in range(n - 1):
    two = min(a[i], a[i + 1])
    if two > 0:
        cost += two * 5
        a[i], a[i + 1] = a[i] - two, a[i + 1] - two

for i in range(n):
    if a[i] > 0:
        cost += a[i]*3
        a[i] = 0

print(cost)
