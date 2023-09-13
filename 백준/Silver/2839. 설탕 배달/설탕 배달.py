# 2839번 : 설탕 배달
# 분류 : 수학, 다이나믹 프로그래밍, 그리디 알고리즘

import sys
input = sys.stdin.readline

n = int(input())
cnt = 0

#5kg 봉지로 모두 나누어 떨어질 때까지 3kg 봉지 사용
while n % 5 != 0 and n >= 0 :
    n -= 3
    cnt += 1

if n % 5 != 0:
    print(-1)
else:
    cnt += n // 5
    print(cnt)