# 2753번 : 윤년
# 분류 : 수학, 구현, 사칙연산

import sys
input = sys.stdin.readline

n = int(input())

if n%400 == 0 or n%4 == 0 and n%100 != 0:
    print(1)
else :
    print(0)