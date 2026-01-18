import sys
from collections import deque

input = sys.stdin.readline

# 위치 노드 객체
# 이동 가능한(연결된) 방향이 3가지:+1, -1 ,2배
# 이동 방법이 여러가지 인 경우 상태를 노드로 두고,
# 이동 가능한 상태들을 모두 앳지로 연결한다.
# class Node:
#     visitied=False
#     def __init__(self, name):
#         self.name = int(name)
#         self.move = [name - 1, name + 1, name * 2]
#
#

# s,d=map(lambda n: Node(int(n)),input().split())
# s, d = [Node(int(n)) for n in input().split()]
s, d = map(int, input().split())
MAX = 100000
visited = set()

q = deque()
q.append((s, 0))
visited.add(s)
while q:
    now = q.popleft()
    n = now[0]
    if n == d:
        print(now[1])
        break
    for next_node in [n - 1, n + 1, n * 2]:
        if next_node in visited or 0 > next_node or next_node > MAX:
            continue
        q.append((next_node, now[1] + 1))
        visited.add(next_node)
