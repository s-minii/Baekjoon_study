# 4949번 : 균형잡힌 세상
# 분류 : 자료구조, 문자열, 스택
# 참고 : chatGPT

import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()

    if s == '.':
        break

    stack = []
    temp = True

    for i in s:
        if i == '(' or i == '[':
            stack.append(i)

        elif i == ')':
            if not stack or stack[-1] == '[':
                temp = False
                break

            elif stack[-1] == '(':
                stack.pop()

        elif i == ']':
            if not stack or stack[-1] == '(':
                temp = False
                break

            elif stack[-1] == '[':
                stack.pop()

    if temp == True and not stack:
        print('yes')
    else:
        print('no')