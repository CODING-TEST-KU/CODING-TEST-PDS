from _collections import deque
from itertools import combinations
import copy


def bfs(lab, virus_positions):
    n, m = len(lab), len(lab[0])

    temp_lab = copy.deepcopy(lab)
    queue = deque(virus_positions)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and temp_lab[nx][ny] == 0:
                temp_lab[nx][ny]=2
                queue.append((nx,ny))

    return temp_lab

def count_safe_area(lab):
    count=0
    for row in lab:
        count+=row.count(0) #0의 개수를 세는 문법
    return count

def solve():
    n,m=map(int, input().split())
    lab=[]

    # 연구소 정보 입력
    for _ in range(n):
        row=list(map(int, input().split()))
        lab.append(row)

    empty_space=[]
    virus_positions=[]

    for i in range(n):
        for j in range(m):
            if lab[i][j]==0:
                empty_space.append((i,j))
            elif lab[i][j]==2:
                virus_positions.append((i,j))

    max_safe_area=0

    for wall_positions in combinations(empty_space,3):
        temp_lab=copy.deepcopy(lab)
        for x,y in wall_positions:
            temp_lab[x][y]=1

        #bfs 돌려서 바이러스 확산
        infected_lab=bfs(temp_lab,virus_positions)

        # 안전 영역 계산
        safe_area=count_safe_area(infected_lab)
        max_safe_area=max(max_safe_area,safe_area)
    print(max_safe_area)

    # if __name__=="__main__":
solve()