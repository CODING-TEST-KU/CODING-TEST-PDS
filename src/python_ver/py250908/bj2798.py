from itertools import combinations

n,m=map(int,input().split())
cards=list(map(int,input().split()))
result=0

# 트리 순회 (3중 반복문 or 조합 사용)

for cards in combinations(cards,3):
    temp_sum=sum(cards)
    if result< temp_sum<=m:
        result=temp_sum
print(result)