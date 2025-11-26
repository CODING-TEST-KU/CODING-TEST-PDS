import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

space = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

# 걸린시간
time = 0

# 아기상어의 위치 x,y
x, y = 0, 0
mx, my = 0, 0

# 아기 상어의 초기 크기 초기화
baby = 2

# 성장이후 모인 성장 포인트
point = 0

# 이동, 즉 탐색은 왼쪽, 위 순(상,좌,우,하)
dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

# 아기상어의 첫 위치 찾기
for row in range(n):
    for col in range(n):
        if space[row][col] == 9:
            x, y = col, row


# 같은 거리에 있는 물고기를 어떻게 잡아먹을건지(순회를 상 -> 왼쪽으로 하면 될듯


# bfs로 큐를 이용해서 가능한 주변 탐색
# 이동 시 먹이의 크기 탐색
# 첫 순회(상하좌우)때 먹이를 찾으면 먹으러 이동
# 첫 순회때 이동할 수 없는 경우 break
#
def bfs():
    global time, x, y, mx, my
    q = deque()
    q.append((x, y, False))

    while q:
        ##todo 여기서 큐에 있는 먹이 위치 빼서 먹으러 이동
        fx, fy, can = q.popleft()
        # 큐에서 꺼내보고 true이면 먹이활동, false이면 큐애서 빼기 (visited로 관리)
        if can:
            # 먹이를 발견하고, 먹으면, 그제서야 이동하는 방식
            # 먹이 위치와 현재 상어위치는 단순 산술 계산하여 적용
            time += abs(mx - fx) + abs(my - fy)
            mx, my = fx, fy
            x, y = fx, fy

            # grow도 여기서 하기
            grow(fx, fy)

        else:
            visited[fx][fy] = False
            x, y = fx, fy

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 맵밖을 벗어난 경우, 이미 큐안에 있는 경우
            if nx < 0 or ny < 0 or nx >= n or ny >= n or visited[nx][ny]:
                continue
            # 먹이가 아기보다 큰 경우
            if space[nx][ny] > baby:
                continue
            # 먹이가 아기와 크기가 같은 경우-> 큐에 넣기(먹이활동 하지 않음)
            if space[nx][ny] == baby:
                visited[nx][ny] = True
                q.append((nx, ny, False))
            # 먹이가 아기보다 크기가 작은 경우 ->큐에 넣기(먹이활동 한다)
            if space[nx][ny] < baby:
                visited[nx][ny] = True
                q.append((nx, ny, True))


# 푸드를 먹으면 푸드 위치를 0으로 바꾸고
# 성장가능한경우 성장한 후 point 초기화, 불가능한 경우 point증가
def grow(fx, fy):
    global point, baby
    space[fx][fy] = 0
    point += 1
    if point == baby:
        baby += 1
        point=0

bfs()
print(time)
