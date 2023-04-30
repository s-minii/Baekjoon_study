# 10816 : 숫자카드 2
# 풀이
# 기존 딕셔너리로 찾는 방법 이외에 counter 클래스를 사용한다.

# counter 클래스를 사용한 방법
from collections import Counter

p_cnt = int(input())
problem = list(map(int, input().split()))
u_cnt = int(input())
user = list(map(int, input().split()))

problem = Counter(problem)


for i in user:
    if i in problem:
        print(problem[i], end = ' ')
    else:
        print('0', end = ' ')