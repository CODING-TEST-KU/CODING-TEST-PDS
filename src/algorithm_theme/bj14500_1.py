import sys

input = sys.stdin.readline

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

ans = 0
visited = [[False] * m for _ in range(n)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


# 한 칸마다 모든 가능한 테트로미노를 탐색한다.

# 하나의 선으로 만들 수 있는 테트로미노 탐색
def dfs(r, c, d, now_sum):
    global ans

    if d == 4:
        ans = max(ans, now_sum)
        return

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
            visited[nr][nc] = True
            dfs(nr, nc, d + 1, now_sum + paper[nr][nc])
            visited[nr][nc] = False


# ㅗ,ㅜ,ㅏ,ㅓ 인 경우 탐색
def shape_t(r, c):
    global ans
    now_sum = paper[r][c]
    count = 0
    min_num = 100000000
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < n and 0 <= nc < m:
            now_sum += paper[nr][nc]
            count += 1
            min_num = min(min_num, paper[nr][nc])

    if count == 4:
        ans = max(ans, now_sum - min_num)
    elif count == 3:
        ans = max(ans, now_sum)


# 모든 칸을 순회
def find_all_single():
    for i in range(n):
        for j in range(m):
            visited[i][j]=True
            dfs(i, j, 1, paper[i][j])
            visited[i][j]=False
            shape_t(i, j)


find_all_single()
print(ans)
