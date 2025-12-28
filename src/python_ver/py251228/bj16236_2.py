import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

# 먹이정보와 아기 상어 위치 받아오기
space = [list(map(int, input().split())) for _ in range(n)]

# 아기상어의 초기 위치 찾기
br, bc = -1, -1
for r in range(n):
    for c in range(n):
        if space[r][c] == 9:
            br, bc = r, c
            space[r][c] = 0
            break

# 아기상어의 크기
baby_size = 2
# 아기상어가 먹은 물고기 수
food = 0
# 아기상어가 엄마 없이 돌아다닌 시간
time = 0

# 이동
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

# 한 판의 단위는 물고기를 먹는 것
# 먹을 수 있는 물고기가 없을 때까지 무한 반복

while True:

    # 거리 초기화
    dist = [[-1 for _ in range(n)] for _ in range(n)]

    # 먹이 리스트 (위치r, 위치c, 거리)
    pray = []

    # 아기상어 위치
    dist[br][bc] = 0
    move = deque()
    move.append((br, bc))

    while move:
        tr, tc = move.popleft()
        for i in range(4):
            nr, nc = tr + dr[i], tc + dc[i]
            # 범위 밖이거나 크기가 큰 물고기 칸
            if 0 > nr or nr >= n or 0 > nc or nc >= n :
                continue
            if space[nr][nc] > baby_size:
                continue
            # 크기가 같은 물고기 칸
            if space[nr][nc] == baby_size and dist[nr][nc] == -1:
                dist[nr][nc] = dist[tr][tc] + 1
                move.append((nr, nc))
            # 크기가 작은 물고기 칸
            if space[nr][nc] < baby_size and dist[nr][nc] == -1:
                dist[nr][nc] = dist[tr][tc] + 1
                if 0 < space[nr][nc] < baby_size:
                    pray.append((nr, nc, dist[nr][nc]))
                move.append((nr, nc))

    if not pray:
        print(time)
        break
    else:
        pray.sort(key=lambda x: (x[2], x[0], x[1]))
        rr, cc, d = pray[0]
        time+=d
        br,bc=rr,cc
        food+=1
        space[br][bc]=0

        if baby_size==food:
            baby_size+=1
            food=0



