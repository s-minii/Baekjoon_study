import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
arr = []
center = N // 2
result = 0
sum = 0

for _ in range(N):
    row = list(map(int, input().split()))
    arr.append(row)

for i in range(N):
    for j in range(N):
        result += arr[i][j]

for i in range(center):
    for j in range(center-i, center+i+1):
        sum += arr[i][j] #다이아몬드 중앙 + 다이아몬드 위
        sum += arr[N-i-1][j] #다이아몬드 중앙 + 다이아몬드 아래

sum -= arr[center][center] #다이아몬드 중앙 중복제거
result -= sum

print(result)