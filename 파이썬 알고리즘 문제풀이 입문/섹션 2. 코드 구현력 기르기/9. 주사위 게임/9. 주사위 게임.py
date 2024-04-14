import sys
from collections import Counter
sys.stdin = open("input.txt", "rt")


N = int(input())
result = []

for i in range(N):
    dice_arr = list(map(int, input().split()))
    dice_cnt = Counter(dice_arr)

    value = max(dice_cnt.values())

    for key, val in dice_cnt.items():
        if val == value:
            break

    if value >= 3:
        result.append(10000 + key * 1000)
    elif value >= 2:
        result.append(1000 + key * 100)
    else:
        result.append(key * 100)

print(max(result))