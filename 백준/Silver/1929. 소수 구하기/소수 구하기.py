# 1929번 : 소수구하기
# 분류 : 수학, 정수론, 소수 판정, 에라토스테네스의 체
# 참고 : https://seongonion.tistory.com/44

import sys
import math
input = sys.stdin.readline

m, n = map(int, input().split())
arr = [True for _ in range(n + 1)]

# 에라토스테네스의 체 알고리즘을 사용하여 소수 판정
for i in range(2, int(math.sqrt(n)) + 1):
    if arr[i] == True:
        j = 2
        while i * j <= n:
            arr[i * j] = False
            j += 1

# 범위 내의 소수 출력
for i in range(m, n + 1):
    if i > 1 and arr[i] == True:
        print(i)