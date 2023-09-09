# 1676번 : 팩토리얼 0의 개수
# 분류 : 수학

import sys
import math
input = sys.stdin.readline


n = int(input())
fac_n = math.factorial(n)
cnt = 0

while fac_n % 10 == 0:
    cnt += 1
    fac_n //= 10

print(cnt)