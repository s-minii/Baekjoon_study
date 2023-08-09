# 6550번 : 피카츄

import sys
input = sys.stdin.readline

word = str(input())

word = word.replace("pi", " ")
word = word.replace("ka", " ")
word = word.replace("chu", " ")

if len(word.strip()) == 0:
    print("YES")
else:
    print("NO")