import sys

def main():
    input = sys.stdin.readline
    n, S = map(int, input().split())
    arr = list(map(int, input().split()))

    def dfs(i: int, current_sum: int) -> int:
        if i == n:
            return 1 if current_sum == S else 0
        return dfs(i + 1, current_sum) + dfs(i + 1, current_sum + arr[i])

    ans = dfs(0, 0)
    if S == 0:
        ans -= 1
    print(ans)

if __name__ == "__main__":
    main()
