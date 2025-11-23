import sys

input = sys.stdin.readline

n, s = map(int, input().split())

nums = list(map(int, input().split()))

def solution(d,summ,act):
    result=0
    if summ == s and act!=0:
        result+=1

    for i in range(d, n):
        summ+=nums[i]
        act+=1
        result += solution(i+1,summ,act)
        summ-=nums[i]
        act-=1
    return result

print(solution(0,0,0))

# import sys
# input = sys.stdin.readline
#
# n, s = map(int, input().split())
# nums = list(map(int, input().split()))
#
# def solution(d, summ, act):
#     result = 0
#     # 지금까지 고른 부분수열의 합이 s라면 (공집합 제외)
#     if summ == s and act != 0:
#         result += 1
#
#     # d번 인덱스 이후에서 계속 골라보기
#     for i in range(d, n):
#         result += solution(i + 1, summ + nums[i], act + 1)
#     return result
#
# print(solution(0, 0, 0))
