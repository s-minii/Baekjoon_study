# 2480번 : 주사위 세개
# 백준 단계별로 풀어보기 : 2. 조건문

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + a*1000)
elif a == b:
    print(1000 + a*100)
elif a == c:
    print(1000 + a*100)
elif b == c:
    print(1000 + b*100)
else:
    print(100 * max(a,b,c))