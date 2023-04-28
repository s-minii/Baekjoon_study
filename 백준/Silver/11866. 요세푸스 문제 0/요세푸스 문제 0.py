# 11866 : 요세푸스 문제 O
# 풀이
# 1~N명의 사람이 원에 있다는 가정하에 K번째 사람을 지속적으로 제거한다.
# 이때, 사람이 제거되는 순서를 (N,K) - 요세푸스 순열이라 한다.
# (7,3) - <3, 6, 2, 7, 5, 1, 4> 이다.

# 참조 : https://dongdongfather.tistory.com/72

from collections import deque

a, b = list(map(int, (input().split())))
n = deque()
result = []

for i in range(1, a+1):
    n.append(i)
# n = [1,2,3,4,5,6,7]

#개행 제거 (/n)
print('<', end ='')

# 7번 반복
while len(n):
    for i in range(1, b):
        n.append(n[0])
        n.popleft()
    print(n.popleft(), end='')

    if len(n):
        print(',', end =' ')
print('>')