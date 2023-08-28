# 10809번 : 알파벳 찾기
# 분류 : 구현, 문자열

import sys
input = sys.stdin.readline

s = input()
str = 'abcdefghijklmnopqrstuvwxyz'

for i in str:
    if i in s:
        print(s.index(i), end =' ')
    else:
        print(-1, end=' ')