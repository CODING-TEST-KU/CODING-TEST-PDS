# 최댓값만 찾으면 됨,
# 모든 칸에서 해당 칸을 포함하면서 가장 큰 합을 저장한다. -> 중복 검사 다수
# 위 방법에서 visited를 사용하면 중복검사문제를 해결할 수 있다.

# 헐 dfs 로는 하나의 선으로 갈 수 있는 경로만 탐색가능하다
# 즉 ㅗ 형태와 ㅜ 형태는 dfs로 갈 수 없으므로 예외처리를 해주어야한다.

import sys
import collections

input = sys.stdin.readline

n, m = map(int, input().split())

nums = [list(map(int, input().split)) for _ in range(n)]

result = 0

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

visit = [[False for _ in range(m)] for _ in range(n)]


def backtrack(r, c, block):
    if len(block) == 4:
        this_sum = 0
        for sr, sc in block:
            this_sum += nums[sr][sc]
        return this_sum

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        # 큐 꼬리의 상하좌우 중 visit이 아니며, 범위에 있는 경우 큐에 넣기
        if visit[nr][nc] or nr < 0 or nr >= n or nc < 0 or nc > m or (nr, nc) in block:
            continue

        block.append((nr, nc))
        backtrack(nr, nc, block)
        block.pop()


def find_max(r, c, nums):
    global result, visit
    # 현재 위치를 큐에 넣고 visit처리
    # 백트래킹
    found_max = 0
    block = [(r, c)]
    # 여기서 블록 4개를 다채우기
    q = []


    result = max(result, found_max)


for x in range(n):
    for y in range(m):
        find_max(x, y, nums)

print(result)
