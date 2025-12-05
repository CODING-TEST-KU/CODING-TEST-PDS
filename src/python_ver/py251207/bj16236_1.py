import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

space = [list(map(int, input().split())) for _ in range(n)]

# 아기상어의 초기 위치 찾기
now_r, now_c = -1, -1
for r in range(n):
    for c in range(n):
        if space[r][c] == 9:
            now_r, now_c = r, c
            space[now_r][now_c]=0


# 시계방향
dc = [-1, 0, 1, 0]
dr = [0, 1, 0, -1]

# 아기상어의 크기
baby = 2
count = 0
eat = 0


# def bfs():
#     global now_r, now_c, count, eat, baby
while True:
    distance = [[-1 for _ in range(n)] for _ in range(n)]
    q = deque()
    q.append((now_r, now_c))
    distance[now_r][now_c] = 0
    # 자신의 주변의 distance가 -1이 아니고,
    # 자신보다 작거나 같은 물고기가 있는 경우 지나감
    fish = []
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr >= n or nr < 0 or nc >= n or nc < 0:
                continue
            if distance[nr][nc] != -1 or space[nr][nc] > baby:
                continue
            if distance[nr][nc] == -1 and space[nr][nc] == baby:
                distance[nr][nc] = distance[r][c] + 1
                q.append((nr, nc))
                continue
            if distance[nr][nc] == -1 and space[nr][nc] < baby:
                distance[nr][nc] = distance[r][c] + 1
                if 0 < space[nr][nc] < baby:
                    fish.append((distance[nr][nc], nr, nc))
                q.append((nr, nc))
                continue
    if not fish:
        print(count)
        exit(0)
    else:
        ####
        fish.sort(key=lambda x:(x[0],x[1],x[2]))
        food=fish[0]
        now_r,now_c=food[1],food[2]
        # min_dis = n * n
        # for fishi in fish:
        #     if min_dis > fishi[0]:
        #         min_dis = fishi[0]
        #         now_r, now_c = fishi[1], fishi[2]
        count += distance[now_r][now_c]
        space[now_r][now_c]=0

        # 성장
        eat += 1
        if eat == baby:
            baby += 1
            eat = 0
