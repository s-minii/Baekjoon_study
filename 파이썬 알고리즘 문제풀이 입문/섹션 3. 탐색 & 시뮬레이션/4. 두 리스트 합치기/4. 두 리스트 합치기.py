import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
N_list = list(map(int, input().split()))

M = int(input())
M_list = list(map(int, input().split()))

nm_list = N_list+M_list
nm_list.sort()

print(*nm_list)