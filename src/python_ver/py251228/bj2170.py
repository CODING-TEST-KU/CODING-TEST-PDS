import sys

input = sys.stdin.readline

n = int(input())
range_list = []
total=0

# 데이터 받아오기
for i in range(n):
    x, y = map(int, input().split())
    range_list.append((x, y))
range_list.sort(key=lambda x: x[0])

tx, ty = range_list[0][0], range_list[0][1]
for x,y in range_list:
    if tx<=x<=ty:
        ty=max(y,ty)
    else:
        total+=ty-tx
        tx,ty=x,y

total+=ty-tx
print(total)

# for j in range(len(range_list)):
#     if range_list[j][0] <= x <= range_list[j][1] or range_list[j][0] <= y <= range_list[j][1]:
#         nx=min(x,range_list[j][0])
#         ny=max(y,range_list[j][1])
#         # 확장한 범위가 다른 범위와 겹치는 지 확인
#         break


# range_set=set()
#
# for i in range(n):
#     x,y=map(int, input().split())
#     for num in range(x,y):
#         range_set.add(num)
#
# print(len(range_set))
