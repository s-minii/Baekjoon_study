# 2751 : 수 정렬하기 2
# 단순하게 Sorted로 풀었다가 시간초과가 떴다.
# import sys, readline을 활용하여 문제를 해결하였다.

import sys
count = int(input())

num = []

for i in range(count):
    #j = int(input())
    num.append(int(sys.stdin.readline()))

s_num = sorted(num)

for i in s_num:
    print(i)