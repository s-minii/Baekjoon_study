# 10989번 : 수 정렬하기 3
# 분류 : 정렬

import sys
input = sys.stdin.readline

n = int(input())
arr = [0] * 10001

for i in range(n):
    arr[int(input())] +=1

for i in range(10001):
    for j in range(arr[i]):
        print(i)