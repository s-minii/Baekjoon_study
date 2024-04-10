import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
arr_N = list(map(int, input().split()))
closely_num = float('inf')

average = round(sum(arr_N) / N)

for idx, x in enumerate(arr_N):
    temp = abs(average - x)
    if temp < closely_num:
        closely_num = temp
        score = x
        result = idx+1
    elif temp == closely_num:
        if x > score:
            score = x
            result = idx+1

print(average, result)