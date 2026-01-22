from collections import deque

n = int(input())
board = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 9:
            sx, sy = i, j
            row[j] = 0
    board.append(row)

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

size = 2
eat = 0
time = 0

def bfs(x, y, size):
    visited = [[False]*n for _ in range(n)]
    q = deque()
    q.append((x, y, 0))
    visited[x][y] = True

    fishes = []
    min_dist = float('inf')

    while q:
        cx, cy, dist = q.popleft()

        if dist > min_dist:
            break

        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if board[nx][ny] <= size:
                    visited[nx][ny] = True
                    if 0 < board[nx][ny] < size:
                        fishes.append((dist + 1, nx, ny))
                        min_dist = dist + 1
                    q.append((nx, ny, dist + 1))
    return fishes

while True:
    fishes = bfs(sx, sy, size)
    if not fishes:
        break

    fishes.sort()
    dist, nx, ny = fishes[0]

    time += dist
    sx, sy = nx, ny
    board[nx][ny] = 0
    eat += 1

    if eat == size:
        size += 1
        eat = 0

print(time)
