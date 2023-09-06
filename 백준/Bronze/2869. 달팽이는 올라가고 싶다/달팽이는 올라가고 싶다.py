# 2775번 : 달팽이는 올라가고 싶다
# 분류 : 수학
# 참고 : chatGPT

import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())
date = (V - B - 1) // (A - B) + 1
print(date)