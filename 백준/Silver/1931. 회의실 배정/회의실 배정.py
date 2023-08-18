# 1931번 : 회의실 배정
# 분류 : 그리디 알고리즘
# 참고 : https://jokerldg.github.io/algorithm/2021/03/11/meeting-room.html

import sys
input = sys.stdin.readline

cnt = int(input())
time = []

for i in range(cnt):
    start, end = map(int, input().split())
    time.append([start, end])

#시작 시간을 기준으로 오름차순
time = sorted(time, key=lambda a: a[0])

#끝나는 시간을 기준으로 다시 오름차순
time = sorted(time, key=lambda a: a[1])

last = 0
result = 0

for i, j in time:
    if i >= last:
        result += 1
        last = j

print(result)