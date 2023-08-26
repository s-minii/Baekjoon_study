# 2577번 : 숫자의 개수
# 분류 : 수학, 사칙연산

import sys
input = sys.stdin.readline

N=int(input())
M=int(input())
K=int(input())
sum = N * M * K

dict_count = {}
for i in range(10):
    dict_count[i] = 0

for i in str(sum):
    x = int(i)
    dict_count[x] +=1

for i in range(10):
    print(dict_count[i])