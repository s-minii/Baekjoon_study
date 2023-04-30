# 10828 : 스택

import sys
input = sys.stdin.readline
cnt = int(input())

stack = []

for i in range(cnt):
    user_input = input().split()

    # push 부분을 해결하지 못했다.
    # push 이후 숫자는 split으로 구분하여 [1]을 추가시켰다.
    if user_input[0] == 'push':
        stack.append(user_input[1])

    elif user_input[0] == 'pop':
        if len(stack) != 0:
            print(stack.pop())
        elif len(stack) == 0:
            print(-1)

    elif user_input[0] == 'size':
        if len(stack) != 0:
            print(len(stack))
        else:
            print(0)

    elif user_input[0] == 'empty':
        if len(stack) != 0:
            print(0)
        if len(stack) == 0:
            print(1)

    elif user_input[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])