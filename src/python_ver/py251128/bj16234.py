import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, L, R = map(int, input().split())
a = []

for r in range(n):
    a.append(list(map(int, input().split())))

# 상 우 하 좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


# 인구수 차이를 검사하여 연합의 정보를 반환하는 메서드
# x,y와 연결된 new_union을 완성해주는 함수
def scan(x, y):
    global new_union
    visited[x][y] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx >= n or nx < 0 or ny >= n or ny < 0 or visited[nx][ny]:
            continue
        if L <= abs(a[x][y] - a[nx][ny]) <= R:
            new_union.append((nx, ny))
            scan(nx, ny)


# 연합별로 인구수를 합하고 평균내어 인구수를 갱신하는 함수
def mix(unions):
    for union in unions:
        total=0
        count=0
        for nation in union:
            total+=a[nation[0]][nation[1]]
            count+=1
        same=total//count
        for nation in union:
            a[nation[0]][nation[1]]=same


ex=True
days = 0

while ex:
    unions=[]
    visited = [[False for _ in range(n)] for _ in range(n)]  # 인구 통합때마다 갱신
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                new_union = [(i, j)]  # 새 유니온 찾을 때마다 갱신
                scan(i, j)
                unions.append(new_union) #  dfs 탐색이 끝난 경우 union.append(new_union)

    # 이번 턴에 실제로 인구 이동이 있었는지 확인
    moved = False
    for union in unions:
        if len(union) > 1:   # 한 칸짜리 말고, 둘 이상 묶였으면 이동 발생
            moved = True
            break

    if not moved :# unions 의 크기가 0이면
        ex=False
    else:
        mix(unions)
        days += 1

print(days)
# 유니온 형태: union=[[(2,3),(2,4)],[(1,2)] ... ]



