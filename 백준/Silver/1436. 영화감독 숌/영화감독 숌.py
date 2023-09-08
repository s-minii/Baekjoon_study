# 1436번 : 영화감독 숌
# 분류 : 브루트포스
# 참고 : https://ji-gwang.tistory.com/231

import sys
input = sys.stdin.readline

n = int(input())

num = 666
cnt = 0

while True:
    if '666' in str(num):
        cnt += 1

        if cnt == n :
            break

    num += 1

print(num)