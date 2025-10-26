import sys

def main():
    n = int(sys.stdin.readline())
    mask = (1 << n) - 1  # 하위 n비트만 사용
    ans = 0

    # cols: 점유된 열들
    # d1  : 점유된 / 대각선들 (row+col 일정) - 다음 행으로 내려가며 << 1
    # d2  : 점유된 \ 대각선들 (row-col 일정) - 다음 행으로 내려가며 >> 1
    def dfs(cols: int, d1: int, d2: int):
        nonlocal ans
        if cols == mask:   # n개의 퀸을 모두 배치
            ans += 1
            return
        # 이번 행에서 배치 가능한 열 비트집합
        avail = ~(cols | d1 | d2) & mask
        # 가능한 자리들을 하나씩 꺼내서 시도 (LSB 분리 트릭)
        while avail:
            bit = avail & -avail
            avail -= bit
            dfs(cols | bit, (d1 | bit) << 1 & mask, (d2 | bit) >> 1)

    dfs(0, 0, 0)
    print(ans)

if __name__ == "__main__":
    main()
