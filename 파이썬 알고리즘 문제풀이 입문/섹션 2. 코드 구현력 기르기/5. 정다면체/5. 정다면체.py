import sys
from collections import Counter
sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())
sum_list = []
max_sums = []

for i in range(1, N+1):
    for j in range(1, M+1):
        sum_list.append(i+j)

result = Counter(sum_list)
max_cnt = max(result.values())

for sum_val, cnt in result.items():
    if cnt == max_cnt:
        max_sums.append(sum_val)

max_sums.sort()

for sum_val in max_sums:
    print(sum_val, end=' ')