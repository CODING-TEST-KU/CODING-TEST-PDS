import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

sea = [list(map(int, input().split())) for _ in range(n)]

baby_shark_size = 2
shark_bally = 0
ans = 0

# 아기상어 위치 찾기
for i in range(n):
    for j in range(n):
        if sea[i][j] == 9:
            baby_r, baby_c = i, j
            sea[i][j] = 0

# 탐색 큐
q = deque()

# 상하좌우
dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]


def find_food():
    global baby_shark_size, shark_bally, ans
    q = deque()
    q.append((baby_r, baby_c, 0))
    visited[baby_r][baby_c] = True
    while q:
        now_r, now_c, dist = q.popleft()
        for i in range(4):
            next_r, next_c = now_r + dr[i], now_c + dc[i]
            if 0 <= next_r < n and 0 <= next_c < n:
                if not visited[next_r][next_c] and sea[next_r][next_c] <= baby_shark_size:
                    visited[next_r][next_c] = True
                    q.append((next_r, next_c, dist + 1))
                    # 상어보다 크기가 작으면 food에 넣기
                    if 0 < sea[next_r][next_c] < baby_shark_size:
                        food.append((next_r, next_c, dist+1))


while True:
    # food, visited 초기화
    food = []
    visited = [[False] * n for _ in range(n)]
    find_food()

    if not food:
        print(ans)
        break
    food.sort(key=lambda x:(x[2], x[0], x[1]))
    eat = food[0]
    baby_r, baby_c = eat[0], eat[1]
    sea[eat[0]][eat[1]] = 0
    shark_bally = shark_bally + 1
    ans = ans + eat[2]
    if shark_bally == baby_shark_size:
        shark_bally = 0
        baby_shark_size = baby_shark_size + 1
