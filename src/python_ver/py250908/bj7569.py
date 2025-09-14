from collections import deque
import sys

dh = [0, 0, 0, 0, -1, 1]
dn = [-1, 1, 0, 0, 0, 0]
dm = [0, 0, -1, 1, 0, 0]


def bfs():
    while q:
        hh, nn, mm = q.popleft()

        for i in range(6):
            n_h = hh + dh[i]
            n_n = nn + dn[i]
            n_m = mm + dm[i]


            if n_h<0 or n_h>=h or n_m<0 or n_m>=m or n_n<0 or n_n>=n:
                continue
            if tomato[n_h][n_n][n_m]==0:
                tomato[n_h][n_n][n_m]=tomato[hh][nn][mm]+1
                q.append((n_h,n_n,n_m))


m, n, h = map(int, input().split())

tomato = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
q = deque()

# 배열 입력받기
for hh in range(h):
    for nn in range(n):
        row = list(map(int, input().split()))
        for mm in range(m):
            tomato[hh][nn][mm] = row[mm]
            if row[mm] == 1:
                q.append((hh, nn, mm))

bfs()

result = 0
for hh in range(h):
    for nn in range(n):
        for mm in range(m):
            if tomato[hh][nn][mm] == 0:
                print(-1)
                sys.exit()
            result = max(result, tomato[hh][nn][mm])

print(result - 1)
