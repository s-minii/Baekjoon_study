# 1654번 : 랜선 자르기
# 분류 : 이분 탐색, 매개 변수 탐색
# 참고 : https://claude-u.tistory.com/443
"""
힌트
802cm 랜선에서 4개, 743cm 랜선에서 3개,
457cm 랜선에서 2개, 539cm 랜선에서 2개를 잘라내 모두 11개를 만들 수 있다.
"""

import sys
input = sys.stdin.readline

K, N = map(int, input().split())

lan = []
for _ in range(K):
    num = int(input())
    lan.append(num)

start = 1
end = max(lan)

while start <= end :
    mid = (start + end) // 2
    lines = 0 #랜선 수

    for i in lan:
        lines += i // mid

    if lines >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)