# 11723 : 집합
# set을 사용하지 않으면 메모리초과, 시간초과 오류가 뜬다.
# remove 대신 discard를 사용한다. (시간 줄이기)


import sys
input = sys.stdin.readline


cnt = int(input())
S = set()

for i in range(cnt):
    user_input = input().split()

    if user_input[0] == 'all' or user_input[0] == 'empty':
        if user_input[0] == 'all':
            S = set(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'])
        elif user_input[0] == 'empty':
            S = set()
    else:
        if user_input[0] == 'add':
            S.add(user_input[1])

        elif user_input[0] == 'remove':
            S.discard(user_input[1])

        elif user_input[0] == 'check':
            if user_input[1] in S:
                print(1)
            else:
                print(0)

        elif user_input[0] == 'toggle':
            if user_input[1] not in S:
                S.add(user_input[1])
            else:
                S.discard(user_input[1])