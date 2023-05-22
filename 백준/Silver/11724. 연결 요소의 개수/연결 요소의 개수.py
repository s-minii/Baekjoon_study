# 11724 : 연결 요소의 개수
# 풀이 : 깊이우선방식으로 접근하였다.
# 참고 : https://great-park.tistory.com/21

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
# 인접 리스트 -> 인덱스를 그대로 정점의 번호로 사용
graph = list([] for _ in range(N+1))

# 연결 요소 개수
cnt = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS
visited = [False] * (N+1)
def DFS(x):
    visited[x] = True

    for node in graph[x]:
        if not visited[node]:
            DFS(node)

for i in range(1, N+1):
    if not visited[i]:
        DFS(i)
        cnt += 1

print(cnt)