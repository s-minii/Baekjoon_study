# 1620 : 나는야 포켓몬 마스터

import sys
input = sys.stdin.readline

a, b = map(int, input().split())

key_id = {}
key_name = {}

for i in range(1, a+1):
    # rstrip()을 붙이지 않으면, 딕셔너리 value 마지막에 \n이 붙는다.
    poketmon = input().rstrip()
    key_id[i] = poketmon
    key_name[poketmon] = i

for i in range(b):
    n = input().rstrip()
    # isdigit() = 숫자
    if n.isdigit():
        print(key_id[int(n)])
    # isalpha() = 문자
    elif n.isalpha():
        print(key_name[n])