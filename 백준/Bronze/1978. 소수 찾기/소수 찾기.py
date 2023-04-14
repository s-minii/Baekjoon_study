# 1978 : 소수 찾기
# 풀이
# 소수 찾는 방법 중 시간복잡도 효율이 가장 좋다는 에라토스테네스의 체 방법을 사용한다.
# 에라토스테네스의 체는 2부터 시작하여 자신의 배수가 되는 수를 지워나간다.
# ex) 120까지의 소수를 구한다고 하면 11^2 > 120이므로, 11보다 작은 수들의 배수를 지운다.
# 
# 1. 값을 리스트로 입력받는다. (띄어쓰기로 구분)
# 2. 소수인지 아닌지 찾아서 출력한다.

import sys

#1
n = int(sys.stdin.readline())
list_n = list(map(int, sys.stdin.readline().split()))
decimal = 0

#2
for i in list_n:
    count = 0
    #0과 1은 소수가 아니다.
    if i == 0 and 1:
        continue
    if i > 1 :
        for j in range(2, i+1):
            if(i%j == 0):
                count += 1
        if(count == 1):
            decimal +=1

print(decimal)