import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline\

###todo 어렵다 ,,, 다시 풀어보기

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

visited = [[False]*m for _ in range(n)]
ans = 0
max_val = max(map(max, a))  # 가지치기용

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def dfs(r, c, depth, total):
    global ans

    # 가지치기: 남은 칸을 전부 max_val로 채워도 ans 못 넘으면 중단
    if total + (4 - depth) * max_val <= ans:
        return

    if depth == 4:
        ans = max(ans, total)
        return

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
            visited[nr][nc] = True
            dfs(nr, nc, depth + 1, total + a[nr][nc])
            visited[nr][nc] = False

def check_t(r, c):
    """
    'ㅗ' 모양 4가지(회전)만 별도로 체크
    중심 (r,c) + 주변 4방 중 3개 선택
    """
    global ans
    wings = []
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < n and 0 <= nc < m:
            wings.append(a[nr][nc])

    if len(wings) < 3:
        return

    center = a[r][c]
    if len(wings) == 3:
        ans = max(ans, center + sum(wings))
    else:
        # 4개 다 있으면 그중 최소 하나 빼서 3개 선택
        ans = max(ans, center + sum(wings) - min(wings))

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, a[i][j])
        visited[i][j] = False
        check_t(i, j)

print(ans)
