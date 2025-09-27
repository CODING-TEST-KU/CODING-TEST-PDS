from collections import deque

n = int(input())
height = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

max_safe = 0
q = deque()

def dfs(h):
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and height[nx][ny] > h and visited[nx][ny]==0:
                visited[nx][ny] = 1
                q.append((nx, ny))

max_h = max(map(max, height)) # 배열 중 가장 큰 원소 찾기
for i in range(max_h):
    safe=0
    visited = [[0 for _ in range(n)] for _ in range(n)]
    q = deque()
    # h 보다 큰 애들 전부 넣기
    for x in range(n):
        for y in range(n):
            if height[x][y] >i and visited[x][y]==0:
                safe+=1
                visited[x][y]=1
                q.append((x, y))
                dfs(i)

    max_safe=max(max_safe,safe)
print(max_safe)