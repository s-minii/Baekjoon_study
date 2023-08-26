# 10871번 : X보다 작은 수
# 분류 : 구현

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
result = []

for i in arr:
    if i < m:
        result.append(i)

print(*result)