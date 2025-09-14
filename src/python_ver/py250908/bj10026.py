dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def dfs(i, j):
    color = grid[i][j]
    visited[i][j] = 1

    for p in range(4):
        nx = i + dx[p]
        ny = j + dy[p]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if visited[nx][ny] == 0 and grid[nx][ny] == color:
            dfs(nx, ny)


def mod_dfs(i, j):
    color = grid[i][j]
    mod_visited[i][j] = 1
    for p in range(4):
        nx = i + dx[p]
        ny = j + dy[p]
        # 범위 체크
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if mod_visited[nx][ny] == 0 and (grid[nx][ny] == color or (color != 'B' and grid[nx][ny] != 'B')):
            mod_dfs(nx, ny)


n = int(input())
grid = [list(input()) for _ in range(n)]

visited = [[0] * n for _ in range(n)]
section = 0

# 모든 칸에 대해 정상인 색 구분
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j)
            section += 1

mod_visited = [[0] * n for _ in range(n)]
mod_section = 0

# 모든 칸에 대해 적록색약 색 구분
for i in range(n):
    for j in range(n):
        if mod_visited[i][j] == 0:
            mod_dfs(i, j)
            mod_section += 1

print(section, mod_section)