import sys

input = sys.stdin.readline


class Person:
    count = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y


def compare(p1, p2):
    if p1.x > p2.x and p1.y > p2.y:
        p2.count += 1
        return
    elif p1.x < p2.x and p1.y < p2.y:
        p1.count += 1
        return

n = int(input())
data = []

# 입력 받기
for i in range(n):
    x, y = map(int, input().split())
    data.append(Person(x, y))

# 본인보다 큰 사람의 수를 세기
for i in range(n):
    for j in range(i + 1, n):
        compare(data[i], data[j])

for p in data:
    print(p.count + 1, end=" ")
