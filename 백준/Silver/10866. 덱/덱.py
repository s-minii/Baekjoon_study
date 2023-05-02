# 10866 : 덱

from collections import deque
import sys
input = sys.stdin.readline

cnt = int(input())
user_input = []
deque = deque()

for i in range(cnt):
    user_input = input().split()

    if user_input[0] == 'push_front':
        deque.appendleft(user_input[1])

    if user_input[0] == 'push_back':
        deque.append(user_input[1])

    if user_input[0] == 'pop_front':
        if len(deque) != 0:
            print(deque[0])
            deque.popleft()
        elif len(deque) == 0:
            print(-1)

    #deque.pop은 덱의 첫 번째 값를 제거하고, 그 값을 출력하는건데 
    # 왜 print([deque[-1])을 넣어야 하는지 모르겠음.
    # 출력이 안 됨. 그래서 print를 넣음.
    if user_input[0] == 'pop_back':
        if len(deque) != 0:
            print(deque[-1])
            deque.pop()
        elif len(deque) == 0:
            print(-1)

    if user_input[0] == 'size':
        print(len(deque))

    if user_input[0] == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)

    if user_input[0] == 'front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])

    if user_input[0] == 'back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])