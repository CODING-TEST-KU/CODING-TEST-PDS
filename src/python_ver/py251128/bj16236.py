import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

space = [list(map(int, input().split())) for _ in range(n)]

# 걸린시간
time = 0

# 아기상어의 위치 sr, sc
sr, sc = 0, 0

# 아기 상어의 초기 크기 초기화
baby = 2

# 성장이후 모인 성장 포인트
point = 0

# 상, 좌, 우, 하
dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

# 아기상어의 첫 위치 찾기
for row in range(n):
    for col in range(n):
        if space[row][col] == 9:
            sr, sc = row, col
            space[sr][sc] = 0
            break


# 같은 거리에 있는 물고기를 어떻게 잡아먹을건지(순회를 상 -> 왼쪽으로 하면 될듯


# bfs로 큐를 이용해서 가능한 주변 탐색
# 이동 시 먹이의 크기 탐색
# 첫 순회(상하좌우)때 먹이를 찾으면 먹으러 이동
# 첫 순회때 이동할 수 없는 경우 break
#
def bfs(sr, sc):
    '''현재 상어 위치에서 한 번의bfs로 먹을 수 있는 가장 가까운 물고기 하나를 찾는다.
    없으면 none, 있으면(물고기 행, 물고기 열, 거리) 반환'''

    global baby
    dist = [[-1] * n for _ in range(n)]

    q = deque()
    q.append((sr, sc))
    dist[sr][sc] = 0

    candidates = []
    min_dist = None

    while q:
        ##todo 여기서 큐에 있는 먹이 위치 빼서 먹으러 이동
        r, c = q.popleft()
        # 큐에서 꺼내보고 true이면 먹이활동, false이면 큐애서 빼기 (visited로 관리)

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            # 맵밖을 벗어난 경우, 이미 큐안에 있는 경우
            if nr < 0 or nc < 0 or nr >= n or nc >= n or dist[nr][nc] != -1:
                continue
            # 먹이가 아기보다 큰 경우
            if space[nr][nc] > baby:
                continue

            # 이동 가능
            dist[nr][nc] = dist[r][c] + 1

            # 먹이가 아기보다 크기가 작은 경우 ->큐에 넣기(먹이활동 한다)
            if 0< space[nr][nc] < baby:
                if min_dist is None or dist[nr][nc]<=min_dist:
                    min_dist=dist[nr][nc]
                    candidates.append((nr,nc,min_dist))

            q.append((nr,nc))

    if not candidates:
        return None

# 푸드를 먹으면 푸드 위치를 0으로 바꾸고
# 성장가능한경우 성장한 후 point 초기화, 불가능한 경우 point증가

    #가장 가까운 거리만 필터링
    candidates=[fish for fish in candidates if fish[2]==min_dist]
    candidates.sort(key=lambda x:(x[0],x[1]))
    return candidates[0]

while True:
    result=bfs(sr,sc)
    if result is None:
        break

    fr, fc, fdist =result
    time+= fdist
    point+=1
    space[fr][fc]=0
    sr,sc=fr,fc

    if point == baby:
        baby += 1
        point = 0

print(time)
