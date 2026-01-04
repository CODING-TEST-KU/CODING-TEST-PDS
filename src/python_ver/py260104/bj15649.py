import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 숫자 중복 체크용 리스트
# n+1 크기로 만들어서 인덱스랑 숫자랑 맞춤
visited = [False] * (n + 1)
stack = []

def backtrack(depth):
    # m개 다 찼을 때가 종료 조건
    if depth == m:
        # 리스트 요소를 문자열로 합쳐서 한 줄로 출력
        print(' '.join(map(str, stack)))
        return

    # 1부터 n까지 사전순으로 탐색
    for i in range(1, n + 1):
        if not visited[i]:
            # 방문 처리하고 스택에 넣기
            visited[i] = True
            stack.append(i)

            # 재귀 호출
            backtrack(depth + 1)

            # 백트래킹
            stack.pop()
            visited[i] = False

backtrack(0)