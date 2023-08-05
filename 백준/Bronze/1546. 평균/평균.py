# 1546번 : 평균

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, (input().split())))
avg = []

M = max(arr)

for i in range(N):
    avg.append(arr[i] * 100/ M)

result = sum(avg)/N
print(result)
