import sys
input = sys.stdin.readline

# 재귀 제한 설정
sys.setrecursionlimit(10000)

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if arr[x][y] == 1:
        arr[x][y] = 0  # 해당 배추 영역 방문 처리
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True

    return False


t = int(input())

# 모든 좌표를 0으로 초기화한 후, 좌표를 입력받아 1로 초기 설정
for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        y, x = map(int, input().split())
        arr[x][y] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j):
                cnt += 1

    print(cnt)