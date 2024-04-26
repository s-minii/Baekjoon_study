import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
arr = []
s=e= N // 2
result = 0

for _ in range(N):
    row = list(map(int, input().split()))
    arr.append(row)

for i in range(N):
    for j in range(s, e+1):
        result += arr[i][j]

    if i<N//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1

print(result)