# 11651번 : 좌표 정렬하기 2
# 분류 : 정렬

import sys
input = sys.stdin.readline

n = int(input())
coordinate = []

for _ in range(n):
    x, y = map(int, input().split())
    coordinate.append((x, y))

coordinate = sorted(coordinate, key = lambda x : (x[1], x[0]))

for i in coordinate:
    print(i[0], i[1])