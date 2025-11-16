#백트래킹
import sys

input=sys.stdin.readline

n,m=map(int, input().split())

visited=[False]*(n+1)
result=[]

def backtracking(depth):
    if depth == m:
        print(" ".join(map(str,result)))
        return

    for i in range(1, n+1):
        if not visited[i]:
            visited[i]=True
            result.append(i)

            #다음 깊이(depth)로 재귀 호출 합니다.
            backtracking(depth+1)
            result.pop()
            visited[i]=False


backtracking(0)