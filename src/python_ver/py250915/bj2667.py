from collections import deque

n = int(input())
house_map = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

house_count = []
q = deque()

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(n):
    for j in range(n):
        if house_map[i][j] == 1 and visited[i][j] == 0:
            q.append((i, j))
            count = 1
            visited[i][j] = 1
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if 0 <= nx < n and 0 <= ny < n :
                        if house_map[nx][ny] == 1 and visited[nx][ny] == 0:
                            q.append((nx, ny))
                            count += 1
                            visited[nx][ny] = 1

            house_count.append(count)

house_count.sort()
print(len(house_count))
for num in house_count:
    print(num)
