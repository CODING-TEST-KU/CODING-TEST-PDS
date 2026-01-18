# 앞에서부터 한번의 스캔으로 끝내는 방식
# 3개가 연속이라면 7/2=2.333333..
# 2개가 연속리아면 5/2=2.5
# 1개가 연속이라면 3

# (2.334 + 3) % 2= 2.667
# 2.667 > 2.5 이므로,
# (3개 연속 +1개 연속) 경우를 (2개 연속 + 2개 연속)으로 대체하는 것이 좋다.


#
import sys

input = sys.stdin.readline

n = int(input())

rm = list(map(int, input().split()))
ans = 0

for i in range(n):

    if i + 2 < n and rm[i + 2] < rm[i + 1]:
        pre_two = min(rm[i],rm[i+1]-rm[i+2])
        rm[i], rm[i + 1] = rm[i] - pre_two, rm[i + 1] - pre_two
        ans += 5 * pre_two

    if i + 2 < n:
        three = min(rm[i], rm[i + 1], rm[i + 2])
        rm[i], rm[i + 1], rm[i + 2] = rm[i] - three, rm[i + 1] - three, rm[i + 2] - three
        ans += 7 * three

    if i + 1 < n:
        two = min(rm[i], rm[i + 1])
        rm[i], rm[i + 1] = rm[i] - two, rm[i + 1] - two
        ans += 5 * two

    ans += 3 * rm[i]

print(ans)
