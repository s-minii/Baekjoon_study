# 18870번 : 좌표 압축
# 숫자를 비교하여 자신보다 작은 숫자 개수를 세면 된다.
# 딕셔너리를 사용하지 않으면 시간초과가 발생한다.

# 딕셔너리를 사용하지 않고, 인덱스 값을 매핑한 경우 시간복잡도 : O(n)
# 딕셔너리를 사용한 경우 시간복잡도 : O(1)

import sys
input = sys.stdin.readline

cnt = int(input())
num = list(map(int, input().split()))
arr = sorted(set(num))

dict = {}

for idx, value in enumerate(arr):
    dict[value] = idx

for value in num:
    print(dict[value], end=" ")