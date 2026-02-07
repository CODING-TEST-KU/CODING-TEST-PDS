import sys

input = sys.stdin.readline

n = int(input())
house = []

# 1:빨강 / 2:초록 / 3:파랑
house_color = [0] * n
for _ in range(n):
    house.append(list(map(int, input().split())))

# dp는 지금까지 만들 수 있는 최소의 비용
dp = [0] * (n + 1)

# if house[0][2] < house[0][3]:
#     dp[0] = house[0][2]
#     house_color[0] = 2
# elif house[0][2] > house[0][3]:
#     dp[0] = house[0][3]
#     house_color[0] = 3
# else:
#     if house[1][2] > house[1][3]:
#         dp[0] = house[0][2]
#         house_color[0] = 2
#     else:
#         dp[0] = house[0][3]
#         house_color[0] = 3

for i in range(1,n):
    # 두단계 이전부터 보면 됨

    # A B C D E ->
    # 1 2 1 1 1
    # a에서
    chosen = house_color[i - 1]
    if chosen == 1:
        if house[i][2] < house[i][3]:
            dp[i] = dp[i - 1] + house[i][2]
            house_color[i] = 2
        elif house[i][2] > house[i][3]:
            dp[i] = dp[i - 1] + house[i][3]
            house_color[i] = 3
        else:
            if house[i + 1][2] > house[i + 1][3]:
                dp[i] = dp[i - 1] + house[i][2]
                house_color[i] = 2
            else:
                dp[i] = dp[i - 1] + house[i][3]
                house_color[i] = 3