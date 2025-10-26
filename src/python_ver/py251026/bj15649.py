import sys

n, m = map(int, sys.stdin.readline().split())

used = [False] * (n + 1)
picked = []
lines = []

def dfs(depth: int):
    if depth == m:
        lines.append(' '.join(map(str, picked)))
        return
    for x in range(1, n + 1):
        if not used[x]:
            used[x] = True
            picked.append(x)
            dfs(depth + 1)
            picked.pop()
            used[x] = False

dfs(0)
sys.stdout.write('\n'.join(lines))
