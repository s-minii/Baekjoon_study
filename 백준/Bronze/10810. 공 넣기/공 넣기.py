# 10810번 : 공 넣기
# 백준 단계별로 풀어보기 : 3. 반복문

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
basket = [0] * (N+1)

for _ in range(M):
    i, j, k = map(int, input().split())
    for n in range(i, j+1):
        basket[n] = k

for i in range(1, N+1):
    print(basket[i], end = ' ')