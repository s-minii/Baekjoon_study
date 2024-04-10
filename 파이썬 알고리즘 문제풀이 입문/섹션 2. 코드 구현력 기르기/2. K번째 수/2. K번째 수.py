import sys
sys.stdin = open("input.txt", "rt")

T = int(input())

for i in range(T):
    N, s, e, k = map(int, input().split())
    N_arr = list(map(int, input().split()))
    N_arr = N_arr[s-1:e]
    N_arr.sort(reverse=False)
    print("#%d %d" %(i+1, N_arr[k-1]))