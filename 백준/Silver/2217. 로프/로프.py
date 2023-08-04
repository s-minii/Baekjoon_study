# 2217번 : 로프
# 종류 : 그리디 알고리즘

import sys
input = sys.stdin.readline

n = int(input())
m = []

for i in range(n):
    m.append(int(input()))

m.sort(reverse=True)
result = []

for j in range(n):
    result.append(m[j]*(j+1))

print(max(result))