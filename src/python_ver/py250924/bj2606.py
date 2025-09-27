from collections import defaultdict

n=int(input())
m=int(input())

computers=[0 for _ in range(n+1)]
network=defaultdict(set) # defaultdict는 collections import 가 필요하다.

for i in range(m):
    x,y=map(int, input().split())
    network[x].add(y)
    network[y].add(x)


def dfs(target):
    for link_com in network[target]:
        if computers[link_com]==0:
            computers[link_com]=1
            dfs(link_com)

dfs(1)

result=0
computers[1] = 1 # 1번 컴퓨터가 고립되었을 경우 -1 이 출력되지 않도록 함

for computer in computers:
    if computer==1:
        result+=1

print(result-1)

