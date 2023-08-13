# 2231번 : 분해합
# 분류 : 브루트포스


import sys
input = sys.stdin.readline

n = int(input())

for i in range(1, n+1):
    num = sum((map(int, str(i))))
    num_sum = i + num

    if num_sum == n:
        print(i)
        break
    if i == n:
        print(0)