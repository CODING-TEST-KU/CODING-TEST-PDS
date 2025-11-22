import sys

input=sys.stdin.readline

n=int(input())

col=[False]*n
diag1=[False]*(2*n-1)
diag2=[False]*(2*n-1)


def solution(r):
    if r==n:
        return 1
    cnt=0
    for c in range(n):
        # 같은 대각선에 위치한 칸들은 모두 (c+r)이 같거나 (c-r+n-1)이 같다.
        if not col[c] and not diag1[c+r] and not diag2[c-r+n-1]:
            col[c]=diag1[c+r]=diag2[c-r+n-1]=True
            cnt+=solution(r+1)
            col[c]=diag1[c+r]=diag2[c-r+n-1]=False
    return cnt

print(solution(0))



