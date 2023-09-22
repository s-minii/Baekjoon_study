# 1874번 : 스택 수열
# 분류 : 자료 구조, 스택
# 참고 : https://zrr.kr/8nGY

import sys
input = sys.stdin.readline

stack = []
op = [] #연산 여부
cnt = 1
temp = True

N = int(input())
for _ in range(N):
    num = int(input())

    #num 이하 숫자까지 스택 push
    while cnt <= num:
        stack.append(cnt)
        op.append('+')
        cnt += 1

    if stack[-1] == num:
        stack.pop()
        op.append('-')

    else:
        temp = False
        break

if temp == False:
    print('NO')
else :
    for i in op:
        print(i)