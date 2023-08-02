# 1697번 : 숨바꼭질
# 종류 : 너비우선탐색
# 참고 : https://chanhuiseok.github.io/posts/baek-14/

import sys
from collections import deque
input = sys.stdin.readline

max_num = 100000
dist = [0] * (max_num+1)

n, k = map(int, input().split())

def bfs():
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            break
        for i in (x-1, x+1, x*2):
            if 0 <= i <= max_num and not dist[i]:
                dist[i] = dist[x] + 1
                q.append(i)

bfs()