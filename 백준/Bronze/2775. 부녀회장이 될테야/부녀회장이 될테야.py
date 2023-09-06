# 2775번 : 부녀회장이 될테야
# 분류 : 수학, 구현, 다이나믹 프로그래밍
# 참고 : https://url.kr/ja9xkp

import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    k = int(input()) # 층
    n = int(input()) # 호수

    people = [i for i in range(1, n + 1)]  # 0층

    for x in range(k):
        new = []
        for y in range(n):
            new.append(sum(people[:y + 1]))  # 아래층의 1~n호 까지의 합
        people = new.copy()
        
    print(people[-1])  # K층 n호