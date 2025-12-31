import sys
import heapq

input = sys.stdin.readline

left_heap = []
right_heap = []

n = int(input())

for i in range(n):
    num = int(input())
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -num)
    else:
        heapq.heappush(right_heap, num)

    if right_heap and (-left_heap[0] > right_heap[0]):
        left_root = - heapq.heappop(left_heap)
        right_root = heapq.heappop(right_heap)

        heapq.heappush(left_heap, -right_root)
        heapq.heappush(right_heap, left_root)

    print(-left_heap[0])
