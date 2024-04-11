import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
num_arr = list(map(int, input().split()))

#각 자릿수의 합을 구하는 함수
def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum

max = -2147000000

for x in num_arr:
    total = digit_sum(x)
    if max < total:
        max = total
        result = x

print(result)