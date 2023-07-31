# 11659번 : 구간 합 구하기 4
# 단순 합계로 구현하여 실패하였다.
# 리스트의 각 자리까지의 합을 미리 저장해둔 뒤, 각 자리의 누적합에서 빼주는 방식으로 구현하였다.
# 참고 : https://hongcoding.tistory.com/159

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
list_N = list(map(int, input().split()))


prefix_sum = [0]
sum = 0

# 누적합 리스트 구하기
for i in list_N:
    sum += i
    prefix_sum.append(sum)

# 구간 합 구하기
for i in range(M):
    first, last = map(int, input().split())
    result = prefix_sum[last] - prefix_sum[first - 1]
    print(result)
