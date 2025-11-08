import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline


n = int(input())
cards = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))
cards.sort()



out = []
for x in nums:
    out.append(str(bisect_right(cards, x) - bisect_left(cards, x)))
print(' '.join(out))
# for num in nums:
#     start, end = 0, len(cards) - 1
#     count = 0
#     while start <= end:
#         mid = int((start + end) / 2)
#         if cards[mid] == num:
#             while mid > 0 and cards[mid-1] == num:
#                 mid -= 1
#
#             while mid < len(cards) and cards[mid] == num:
#                 mid += 1
#                 count += 1
#             break
#
#         elif cards[mid] < num:
#             start = mid + 1
#         else:
#             end = mid - 1
#     print(count, end=" ")
