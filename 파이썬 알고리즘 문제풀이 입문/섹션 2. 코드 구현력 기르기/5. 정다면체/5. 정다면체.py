# import sys
# from collections import Counter
# sys.stdin = open("input.txt", "rt")

# N, M = map(int, input().split())
# sum_list = []
# max_sums = []
#
# for i in range(1, N+1):
#     for j in range(1, M+1):
#         sum_list.append(i+j)
#
# result = Counter(sum_list)
# max_cnt = max(result.values())
#
# for sum_val, cnt in result.items():
#     if cnt == max_cnt:
#         max_sums.append(sum_val)
#
# max_sums.sort()
#
# for sum_val in max_sums:
#     print(sum_val, end=' ')

import sys
#sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())
arr = [0]*(N+M+1)
max = 0

# 배열에 값 넣는 작업
for i in range(1, N+1):
    for j in range(1, M+1):
        arr[i+j]+=1

# 가장 큰 값의 인덱스 뽑음
for i in range(N+M+1):
    if max < arr[i]:
        max = arr[i]

for i in range(N+M+1):
    if max == arr[i]:
        print(i, end = ' ')