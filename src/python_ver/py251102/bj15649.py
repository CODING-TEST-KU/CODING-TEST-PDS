import sys
input = sys.stdin.readline

N, M = map(int, input().split())
used = [False] * (N + 1)
path = []
out_lines = []

def dfs(depth):
    if depth == M:
        out_lines.append(" ".join(map(str, path)))
        return
    for num in range(1, N + 1):
        if not used[num]:
            used[num] = True
            path.append(num)
            dfs(depth + 1)
            path.pop()
            used[num] = False

dfs(0)
print("\n".join(out_lines))
