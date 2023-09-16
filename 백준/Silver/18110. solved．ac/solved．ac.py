# 18110번 : solved.ac
# 분류 : 수학, 구현, 정렬
# 참고 : https://papapapa.tistory.com/102

import sys
input = sys.stdin.readline

n = int(input())
trim = 0 #절사평균

if n == 0:
    print(0)
else:
    arr = []
    for _ in range(n):
        nan = int(input())
        arr.append(nan)
    arr = sorted(arr)

    # 파이썬에서 round는 5를 초과할 때 반올림한다.
    trim = round(n * 0.15 + 0.0000001)
    trim_sum = sum(arr[trim:n-trim])
    trim_avg = round((trim_sum / (n-2*trim) + 0.0000001))
    print(trim_avg)