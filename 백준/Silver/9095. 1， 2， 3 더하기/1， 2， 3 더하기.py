# 9095번 : 1, 2, 3 더하기
# 풀이 : 1, 2, 3의 케이스를 제외하고 4 이후의 숫자는 앞 3개의 숫자를 더한 값과 같다는 규칙을 발견하였다.

cnt = int(input())

def sol(n):
    # 1, 2, 3의 케이스는 규칙에 해당되지 않아 고정
    if n == 1:
        return 1

    elif n == 2:
        return 2

    elif n == 3:
        return 4

    else:
        return sol(n-1) + sol(n-2) + sol(n-3)

for i in range(cnt):
    n = int(input())
    print(sol(n))
