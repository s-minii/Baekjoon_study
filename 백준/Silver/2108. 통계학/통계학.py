# 2108번 : 통계학
# 분류 :

import sys
import collections
input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    num = int(input())
    arr.append(num)

arr = sorted(arr)

#산술 평균
arithmetic_mean = sum(arr)/ N

#중앙값
median = arr[len(arr) // 2]

#최빈값 (chatgpt)
counter = collections.Counter(arr) # 1. collections를 사용하여 각 빈도수 계산
max_count = max(counter.values())  # 2. 빈도수 중 최대값 찾기

# 3. 가장 큰 값이 여러 개인 경우를 생각해서, mode에 넣고 정렬
mode = []
for key, value in counter.items():
    if value == max_count:
        mode.append(key)
mode = sorted(mode)

# 4. mode중에서 두 번째로 작은 최빈값 찾기
if len(mode) > 1:
    mode = mode[1]  # 두 번째로 작은 최빈값
else:
    mode = mode[0]

#범위
range_num = max(arr) - min(arr)


print(round(arithmetic_mean))
print(round(median))
print(mode)
print(range_num)