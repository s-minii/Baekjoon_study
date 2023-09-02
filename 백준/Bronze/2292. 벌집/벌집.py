# 2292번 : 벌집
# 분류 : 수학

import sys
input = sys.stdin.readline

n = int(input())
num = 1
cnt = 1

while n > num:
    num += 6 * cnt
    cnt += 1

print(cnt)