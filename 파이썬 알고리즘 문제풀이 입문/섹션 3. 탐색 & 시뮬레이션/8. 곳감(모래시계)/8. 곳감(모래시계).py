import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
m = int(input())

for i in range(m):
    h, t, k = map(int, input().split())
    if t == 0 :
        for _ in range(k):
            arr[h-1].append(arr[h-1].pop(0))
    else:
        for _ in range(k):
            arr[h-1].insert(0, arr[h-1].pop())

result = 0
s = 0
e = N-1

for i in range(N):
    for j in range(s, e+1):
        result += arr[i][j]
    if i < N //2 :
        s+=1
        e-=1
    else:
        s-=1
        e+=1

print(result)