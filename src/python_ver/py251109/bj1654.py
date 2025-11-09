import sys

k, n = map(int, input().split())
lines = [int(sys.stdin.readline()) for _ in range(k)]

# 이분탐색으로 일단 적정 길이를 찾아가는 로직을 만들고,
# 각 길이별로 로프의 길이를 나누었을때 몫을 합해서 적정 길이를 넘는 지 확인
# 이분탐색은 그냥 최적화의 수단으로만 사용된다.

start, end = 1, max(lines)

while start <= end:
    mid = (start + end) // 2
    count = 0
    for line in lines:
        count += line // mid

    if count >= n:
        # count==n 인 경우에는 더 긴 길이도 시도할 수 있으므로 mid는 후보가 된다.
        start = mid + 1
    else:
        # end는 딱맞는 길이보다 살짝 짧은 쪽에서 마지막으로 성공했던 값
        end = mid - 1

print(end)
