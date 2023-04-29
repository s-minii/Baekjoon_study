# 9012 : 괄호
# 풀이
# 1. 괄호가 열린 개수(+1)와 닫힌 개수(-1)가 같아야 YES를 한다.
# (예외 : 열리기 전에 닫힐 경우(sum < 0)에 NO를 출력
# 2. 괄호가 닫히지 않은 경우를 NO라 한다.

# 배열로 받아서 쪼개려고 하니까 답이 나오지 않았다.
# 값을 입력받아 리스트로 처리하여 문제를 해결하였다.

cnt = int(input())

for i in range(cnt):

    bracket = input()
    list_bracket = list(bracket)
    sum = 0

    for j in list_bracket:

        if j == '(':
            sum += 1

        elif j == ')':
            sum -= 1

        if sum < 0:
            print('NO')
            break

    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')