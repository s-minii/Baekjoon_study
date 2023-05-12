# 1764 : 듣보잡

import sys
input = sys.stdin.readline

a, b = map(int, input().split())
n = []
m = []

for i in range(a):
    x = input().rstrip()
    n.append(x)

for i in range(b):
    x = input().rstrip()
    m.append(x)

result = sorted(list(set(n) & set(m)))
print(len(result))

for i in result:
    print(i)