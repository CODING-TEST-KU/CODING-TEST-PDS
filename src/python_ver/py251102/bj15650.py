import sys
input = sys.stdin.readline

N, M = map(int, input().split())
path = []
out = []

def dfs(start, depth):
    if depth == M:
        out.append(" ".join(map(str, path)))
        return
    for num in range(start, N + 1):
        path.append(num)
        dfs(num + 1, depth + 1)
        path.pop()

dfs(1, 0)
print("\n".join(out))
