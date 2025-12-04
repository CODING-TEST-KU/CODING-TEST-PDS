import sys

input = sys.stdin.readline

h, w, n, m = map(int, input().split())

# avail = [[False] * w for _ in range(h)]
# count = 0
#
# def sit(r, c):
#     for i in range(n+1):
#         for j in range(m+1):
#             if r + i < h and c + j < w :
#                 avail[r + i][c + j] = True
#
#
# for r in range(h):
#     for c in range(w):
#         if not avail[r][c]:
#             count += 1
#             sit(r, c)

###
# 우리가 원하는 계산 결과를 얻기 위해서는 두 가지 경우를 커버하는 방법을 찾아야한다.
# w를 (m+1)로 나누었을 때
# (1) 나머지가 있을 경우: 몫 +1
# (2) 나머지가 없을 경우: 몫 +0
#
# (1) 의 경우는 나머지가 항상 1보다 크고 (m+1)보다 작으므로, 몫이 +1이 되기 위해서는
#      w에 m(나누려는 수보다 1만큼 작은 수)을 더해주어야한다.
# (2) 의 경우에는 나머지가 0이므로 w에 m만큼 더한 후, (m+1)을 나누어도
#      w를 (m+1)바로 나눈 경우와 결과값 차이가 없으므로 w 대신 w+m으로 계산해도 문제가 없다.

row_max=(h+n)//(n+1)
col_max=(w+m)//(m+1)
count=row_max*col_max

print(count)


#gpt의 설명


# w를 (m+1)로 나눌 때,
# - 나머지가 있으면 몫을 1 올려야 하고
# - 나머지가 없으면 그대로 사용해야 한다.
#
# 이 두 경우를 하나의 식으로 처리하기 위해 w에 m을 더한 뒤 (m+1)로 나눈다.
#
# 이유:
# 1) 나머지가 있는 경우
#    w ÷ (m+1)의 나머지는 1~m 범위이므로,
#    w에 m을 더하면 자연스럽게 몫이 1 증가하여 올림 효과가 발생한다.
#
# 2) 나머지가 없는 경우
#    w가 (m+1)의 배수이므로 w에 m을 더해도 몫이 바뀌지 않아
#    불필요한 올림이 발생하지 않는다.
#
# 따라서 (w + m) ÷ (m+1)을 사용하면
# 나머지 유무에 따라 올림/그대로 처리가 자동으로 이루어진다.
