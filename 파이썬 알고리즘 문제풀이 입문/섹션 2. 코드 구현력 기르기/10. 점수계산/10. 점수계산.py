import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
result = 0
t = 0

num = list(map(int, input().split()))

for i in range(N):
    if num[i] == 0:
        t = 0
    else:
        t += 1
        result += t

print(result)