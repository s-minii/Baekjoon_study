# 14681번 : 사분면 고르기
# 백준 단계별로 풀어보기 : 2. 조건문

import sys
input = sys.stdin.readline

x = int(input())
y = int(input())

if x > 0 and y > 0:
    print('1')
elif x < 0 and y > 0:
    print('2')
elif x < 0 and y < 0:
    print('3')
else:
    print('4')