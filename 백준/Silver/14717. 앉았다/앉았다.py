# 14717번 : 앉았다.
# 분류 : 브루트포스
# 참고 : https://isaaclee.tistory.com/18

import sys
input = sys.stdin.readline
from itertools import permutations

# 카드 저장
card = []
for i in range(1, 11):
    card.append(i)
card = sorted(card * 2)

n = list(map(int, input().split()))

# 중복된 카드 제거
card.remove(n[0])
card.remove(n[1])

# 순열을 이용한 족보 생성 (import)
rank = list(permutations(card, 2))
rank.sort(key=lambda x: (x[0] == x[1], (x[0] + x[1]) % 10, x[0]))

# n(내 카드)이 '땡'인 경우
if n[0] == n[1]:
    print('%.3f' % (1 - ((10 - n[0]) * 2) / len(rank)))

# n(내 카드)이 '끗'인 경우
else:
    c = 0
    for i in rank:
        # 내가 뽑은 패와 같아졌을 경우, break
        if sum(i) % 10 >= sum(n) % 10:
            break
        else:
            c += 1
    print('%.3f' % (c / len(rank)))