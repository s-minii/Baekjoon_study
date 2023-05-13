# 1003 : 피보나치 함수
# 피보나치 함수를 이용한 정석(?)대로 풀이하면 시간초과가 발생한다.
# 이를 해결하기 위해 2까지 미리 선언하여 계산하지 않게하였다.

def fibonacci(n):
    zero = [1, 0, 1]
    one = [0, 1, 1]
    if n >= 3:
        for i in range(2, n):
            zero.append(zero[i-1] + zero[i])
            one.append(one[i-1] + one[i])
    print(zero[n], one[n])

cnt = int(input())

for i in range(cnt):
    k = int(input())
    fibonacci(k)