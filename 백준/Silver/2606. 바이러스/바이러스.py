# 2606 : 바이러스
# 참고 : https://jiwon-coding.tistory.com/93
# 해설 : BFS 알고리즘

computer = int(input())
cnt = int(input())

#경로를 저장하기 위한 2차원 리스트
graph = [[] * computer for _ in range(computer + 1)]

#총 cnt개의 간선을 입력받아 경로를 변수 graph에 저장
for _ in range(cnt):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


result = 0
visited = [0] * (computer + 1)

def dfs(start):
    global result
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)
            result += 1

dfs(1)
print(result)