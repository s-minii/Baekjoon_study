# 10816 : 숫자카드 2
# 풀이
# 딕셔너리를 통해 키를 카운트하여 총 횟수를 저장하고, 출력한다.

p_cnt = input()
problem = sorted(map(int, input().split()))

u_cnt = input()
user = list(map(int, input().split()))

n = {}

# 딕셔너리(n)에 problem 사전의 각 숫자의 등장 횟수를 저장한다.
# n = {-10: 2, 2: 1, 3: 2, 6: 1, 7: 1, 10: 3}

for i in problem:
    if i in n:
        n[i] += 1
    else :
        n[i] = 1

for i in user:
    if i in n:
        print(n[i], end = ' ')
    else:
        print('0', end = ' ')