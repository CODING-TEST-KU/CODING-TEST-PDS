# 최댓값만 찾으면 됨,
# 모든 칸에서 해당 칸을 포함하면서 가장 큰 합을 저장한다. -> 중복 검사 다수
# 위 방법에서 visited를 사용하면 중복검사문제를 해결할 수 있다.

# 헐 dfs 로는 하나의 선으로 갈 수 있는 경로만 탐색가능하다
# 즉 ㅗ 형태와 ㅜ 형태는 dfs로 갈 수 없으므로 예외처리를 해주어야한다.

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

nums = [list(map(int, input().split())) for _ in range(n)]

result = 0

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

visit = [[False] * m for _ in range(n)]


def dfs(r, c, depth, s):
    global result

    if depth == 4:
        result = max(result, s)
        return

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        # 큐 꼬리의 상하좌우 중 visit이 아니며, 범위에 있는 경우 큐에 넣기
        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            continue
        if visit[nr][nc]:
            continue

        visit[nr][nc] = True
        dfs(nr, nc, depth+1, s+nums[nr][nc])
        visit[nr][nc] = False


def find_max(r, c):
    global result
    # DFS 경로로 만들 수 있는 모양
    visit[r][c] = True
    block = [(r, c)]
    dfs(r, c, 1, nums[r][c])
    visit[r][c] = False

    # ㅗ 모양 예외처리
    center = nums[r][c]
    arms = []
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < n and 0 <= nc < m:
            arms.append(nums[nr][nc])

    if len(arms) >= 3:
        if len(arms) == 4:
            result = max(result, center + sum(arms) - min(arms))
        else:
            result = max(result, center + sum(arms))


for x in range(n):
    for y in range(m):
        find_max(x, y)

print(result)
