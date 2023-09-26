# 25304번 : 영수증
# 백준 단계별로 풀어보기 : 2. 조건문

import sys
input = sys.stdin.readline

X = int(input())
N = int(input())
arr = []

for i in range(N):
    a, b = (map(int, input().split()))
    arr.append(a*b)

if X == sum(arr):
    print('Yes')
else:
    print('No')