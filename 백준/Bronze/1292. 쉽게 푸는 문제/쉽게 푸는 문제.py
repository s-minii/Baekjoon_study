# 1292 : 쉽게 푸는 문제

import sys
input = sys.stdin.readline

a, b = map(int, input().split())
arr = []
sum = 0

for i in range(1, b+1):
    for j in range(i):
        arr.append(i)

for i in range(a-1, b):
    sum +=arr[i]

print(sum)

