from collections import deque

m,n=map(int,input().split())
tomatos=[list(map(int, input().split())) for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

q=deque()

def dfs():
    # 먼저 큐에 익은 토마토 위치를 다 넣기
    for i in range(n):
        for j in range(m):
            if tomatos[i][j]==1:
                q.append((i,j))
    # 큐가 빌 때까지 익힘 반복, 이때,이전 토마토 +1의 값을 토마토에 저장
    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if 0<=nx<n and 0<=ny<m and tomatos[nx][ny]==0:
                q.append((nx,ny))
                tomatos[nx][ny]=tomatos[x][y]+1


dfs()
# 가장 큰 값 찾기
max_tom=-1

for line in tomatos:
    for tomato in line:
        if tomato==0:
            print(-1)
            exit(1)
        max_tom=max(max_tom, tomato)

if max_tom==1:
    print(0)
else:
    print(max_tom-1)