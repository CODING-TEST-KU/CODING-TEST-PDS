import sys

input = sys.stdin.readline

n, m = map(int, input().split())

result = []
visited=[False]*(n+1)


def backtracking(depth, num):
    if depth == m:
        print(" ".join(map(str, result)))
        return

    for i in range(num, n + 1):
        if not visited[i]:
            result.append(i)
            visited[i]=True
            backtracking(depth + 1, i)
            result.pop()
            visited[i]=False


backtracking(0, 1)
