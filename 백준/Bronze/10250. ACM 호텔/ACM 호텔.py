# 10250번 : ACM 호텔
# 분류 : 수학, 구현, 사칙연산
# 참고 : https://ooyoung.tistory.com/88

import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    H, W, N = map(int, input().split())
    num = N//H + 1
    floor = N % H
    
    if N % H == 0:
        num = N // H
        floor = H
    print(f'{floor*100+num}')