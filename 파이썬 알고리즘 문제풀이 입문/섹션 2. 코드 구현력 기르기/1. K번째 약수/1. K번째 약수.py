import sys
sys.stdin = open("input.txt", "rt")

N, K = map(int, input().split())
cnt = 0

for i in range(1, N+1):
    if N % i == 0:
        cnt += 1

    if K == cnt:
        print(i)
        break
else:
    print(-1)