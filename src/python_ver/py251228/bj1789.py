import sys

input = sys.stdin.readline

n = int(input())

# (t-1)*t / 2 < n <= t*(t+1) / 2 룰 만족하는 t 값을 찾기
i = 1
while True:
    summ = i * (i + 1) / 2
    if summ <= n:
        i += 1
        continue
    # elif summ == n:
    #     print(n)
    #     exit(1)
    else :
        print(i-1)
        exit(0) ##프로그램 정상 종료는 1이 아니라 0


