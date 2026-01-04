import sys

def solve():
    data = sys.stdin.read().split()
    if not data: return

    n = int(data[0])
    # 인덱스 에러 방지용 패딩 (뒤에 0 0)
    a = list(map(int, data[1:])) + [0, 0]

    ans = 0

    for i in range(n):
        #  i+1이 i+2보다 많을 때 고려
        # 3개 묶기 전에 i랑 i+1 먼저 짝지어서 높이 맞추기
        # 안 그러면 나중에 i+1만 남아서 손해봄
        if a[i+1] > a[i+2]:
            diff = min(a[i], a[i+1] - a[i+2])
            ans += 5 * diff
            a[i] -= diff
            a[i+1] -= diff

        #  3개 세트 (7원)
        # 셋 중 최솟값만큼 빼주기
        v3 = min(a[i], a[i+1], a[i+2])
        ans += 7 * v3
        a[i] -= v3
        a[i+1] -= v3
        a[i+2] -= v3

        # 2개 세트 (5원)
        v2 = min(a[i], a[i+1])
        ans += 5 * v2
        a[i] -= v2
        a[i+1] -= v2

        #  1개 단품 (3원)
        ans += 3 * a[i]

    print(ans)

# 전역변수보다 함수 내부 지역변수가 빨라서 solve()에 몰아넣음
if __name__ == "__main__":
    solve()