import sys
sys.stdin = open("input.txt", "rt")

N, K = map(int, input().split())
arr = list(map(int, input().split()))
sum_set = set()

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum_set.add(arr[i] + arr[j] + arr[k])

sum_arr = list(sum_set)
sum_arr.sort(reverse=True)

print(sum_arr[K-1])