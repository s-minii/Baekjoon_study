# 1744번 : 수묶기 (그리디 알고리즘)

import sys
input = sys.stdin.readline

n = int(input())

plus = []
minus = []
result = 0

for i in range(n):
    m = int(input())
    if m > 1:
        plus.append(m)
    elif m <= 0:
        minus.append(m)
    else:
        result += m

plus.sort(reverse=True)
minus.sort()

for i in range(0, len(plus), 2):
    if i+1 >= len(plus):
        result += plus[i]
    else:
        result += (plus[i] * plus[i+1])

for i in range(0, len(minus), 2):
    if i+1 >= len(minus):
        result += minus[i]
    else:
        result += (minus[i] * minus[i+1])

print(result)