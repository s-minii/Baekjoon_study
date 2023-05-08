# 2693 : N번째 큰 수

import sys
input = sys.stdin.readline

cnt = int(input())
a = []

for i in range(cnt):
    a = list(map(int, input().split()))
    a.sort()
    print(a[-3])