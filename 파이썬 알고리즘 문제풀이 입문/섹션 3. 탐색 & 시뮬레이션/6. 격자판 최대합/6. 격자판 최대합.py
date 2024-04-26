import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
arr = []
max_sum = 0
largest = -2147000000

for _ in range(N):
    row = list(map(int, input().split()))
    arr.append(row)

#행, 열의 합
for i in range(N):
    sum1 = 0
    sum2 = 0

    for j in range(N):
        sum1 += arr[i][j] #행
        sum2 += arr[j][i] #열

    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

sum1 = 0
sum2 = 0

#대각선 합
for i in range(N):
    sum1 += arr[i][i]
    sum2 += arr[i][N-i-1]

if sum1 > largest:
    largest = sum1
if sum2 > largest:
    largest = sum2

print(largest)