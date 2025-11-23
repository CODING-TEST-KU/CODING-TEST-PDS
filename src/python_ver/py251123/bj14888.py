import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
plu, minus, mul, div = map(int, input().split())
maxr = -10 ** 9 * 100
minr = 10 ** 9 * 100


def solution(dep, cur, plu, minus, mul, div):
    global maxr, minr
    if dep == n:
        maxr = max(maxr, cur)
        minr = min(minr, cur)
        return

    if plu > 0:
        solution(dep + 1, cur + nums[dep], plu - 1, minus, mul, div)

    if minus > 0:
        solution(dep + 1, cur - nums[dep], plu, minus - 1, mul, div)

    if mul > 0:
        solution(dep + 1, cur * nums[dep], plu, minus, mul - 1, div)

    if div > 0:
        if cur < 0:
            nex = -((-cur) // nums[dep])
        else:
            nex = cur // nums[dep]
        solution(dep + 1, nex, plu, minus, mul, div - 1)


solution(1, nums[0], plu, minus, mul, div)
print(maxr)
print(minr)
