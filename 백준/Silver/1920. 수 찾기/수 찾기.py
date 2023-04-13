# 1920 : 수 찾기
# 풀이
# 1. 값을 입력받는다.
 # 첫 번째 숫자 n은 수가 존재하는지 기준이 되는 값의 개수이다.
 # n개의 정수를 입력
 # 두 번째 숫자 m은 찾고 싶은 숫자의 개수이다.
 # m개의 비교할 숫자 입력
# 2. 기준이 되는 숫자와 비교하는 숫자를 비교하여, 같으면 1, 틀리면 0 출력

import sys

# 1. 값을 입력받아서 각 자리를 리스트로 나눈다. (set을 통한 중복제거)
n = sys.stdin.readline()
l_n = set(map(int, sys.stdin.readline().split()))

m = sys.stdin.readline()
l_m = list(map(int, sys.stdin.readline().split()))

# 2. l_m[i]가 l_n에 있는가?
for i in range(len(l_m)):
    if l_m[i] in l_n:
        print(1)
    else:
        print(0)