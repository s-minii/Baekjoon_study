# 3052번 : 나머지
# 분류 : 수학, 사칙연산

import sys
input = sys.stdin.readline

n = []

for i in range(10):
    A = int(input())
    B = A % 42
    n.append(B)

set_n = set(n)
print(len(set_n))