# 2439번 : 별찍기 - 2
# 분류 : 수학, 구현, 사칙연산

import sys
input = sys.stdin.readline

n = int(input())

for i in range(1, n+1):
    space = " " * (n-i)
    star = "*" * i
    print(space + star)