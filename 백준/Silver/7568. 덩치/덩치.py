# 7568번 : 덩치
# 분류 : 구현, 브루트포스 알고리즘

import sys
input = sys.stdin.readline


n = int(input())
human = []
cnt =0

for _ in range(n):
    x, y = map(int, input().split())
    human.append((x, y))

for i in human:
    rank = 1
    for j in human:
        if i == j:
            continue

        # 덩치가 제일 큰 사람이 1, 이후 작은 순위
        if i[0] < j[0] and i[1] < j[1]:
            rank +=1

    print(rank, end=' ')