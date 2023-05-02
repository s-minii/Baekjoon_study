# 10845 : 큐

import sys
input = sys.stdin.readline

cnt = int(input())
user_input = []
queue = []

for i in range(cnt):
    user_input = input().split()

    if user_input[0]== 'push':
        queue.append(user_input[1])

    if user_input[0] == 'pop':
        if len(queue) != 0:
            print(queue[0])
            queue.remove(queue[0])
        elif len(queue) == 0:
            print(-1)

    if user_input[0] == 'size':
        print(len(queue))

    if user_input[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else :
            print(0)

    if user_input[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    if user_input[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])