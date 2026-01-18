# 세로 선 관리
# 잘라야하는 선, 자르면 안되는 선, 상관 없는 선
# 잘라야하는 선: 인접한 면 두개의 상태가 다른경우
# 자르면 안되는 선: 인접한 두 면이 모두 나무인 경우
# 상관 없는 선: 인접한 두 면이 모두 나무가 아닌 경우


# 00xx00
# 00x00x
# xxxx00
# ->
# <세로선>
# nymyn
# nyyny
# mmmyn
#
# <가로선>
# nnmyny
# yymyny

# 반직선을 사용할 수 있는 경우: 끝이 n(2)으로 막혀있지 않고,
# 선의 끝까지 세었을때 드는 비용보다 많은 y(1) 가 있는 경우
# 선의 끝이 막혀있는 경우, 그냥 정확하게 잘라야함
# 위 과정을 각 선의 y(1) 위치마다 양쪽 다 해보고 합을 구한 후
# 가장 저렴한 경우를 결과에 저장

# 위 단계를 모든 세로선 가로선마다 진행,

# 가로 선 관리


import sys

MAX = 100000000
input = sys.stdin.readline

n, m, f = map(int, input().split())

wood = [list(input().rstrip()) for _ in range(n)]

# 가로선 추출
row_line = []
for i in range(n - 1):
    a = []
    for j in range(m):
        if wood[i][j] != wood[i + 1][j]:
            a.append(1)
        elif wood[i][j] == "#" or wood[i + 1][j] == "#":
            a.append(2)
        else:
            a.append(0)
    row_line.append(a)

# 세로선 추출
col_line = []
for j in range(m - 1):
    a = []
    for i in range(n):
        if wood[i][j] != wood[i][j + 1]:
            a.append(1)
        elif wood[i][j] == "#" and wood[i][j + 1] == "#":
            a.append(2)
        else:
            a.append(0)
    col_line.append(a)

#
# # 반직선 가능한지 확인하고 최소값 반환하는 함수
# def labor(line):
#     # 반직선 불가능
#     if 2 in line:
#         return line.count(1)
#     else:
#         return f


# 선 한 줄만 가져왔을 때
def scan_line(aline):
    L = len(aline)
    left = 0
    right = L - 1

    # 왼쪽 끝에서 첫 2 까지의 1개수
    left1 = 0
    while left < L and aline[left] != 2:
        if aline[left] == 1:
            left1 += 1
        left += 1

    # 오른쪽 끝에서 첫 2 까지의 1개수
    right1 = 0
    while right >= 0 and aline[right] != 2 and right >= left:
        if aline[right] == 1:
            right1 += 1
        right -= 1

    # 양쪽이 2로 막힌 구간에서 1의 개수
    mid1 = 0
    for i in range(left, right + 1):
        if aline[i] == 1:
            mid1 += 1

    return min(f, left1) + min(f, right1) + mid1


ans = 0

# 가로선 전부
for l in row_line:
    ans += scan_line(l)

# 세로선 전부
for l in col_line:
    ans += scan_line(l)

print(ans)