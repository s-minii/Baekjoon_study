# 9461번 : 파도반 수열
# 분류 : 다이나믹 프로그래밍

import sys
input = sys.stdin.readline

cnt = int(input())

def pado(n):

    if n <= 3:
        return 1

    p = [0] * (n+1)

    p[0] = p[1] = p[2] = 1
    p[3] = p[4] = 2

    for i in range(5, n+1):
        p[i] = p[i-2] + p[i-3]

    return p[n-1]

for _ in range(cnt):
    n = int(input())
    print(pado(n))