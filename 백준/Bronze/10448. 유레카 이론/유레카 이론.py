# 10448번 : 유레카이론
# 분류 : 브루트포스
# 참고 : https://claude-u.tistory.com/376

import sys
input = sys.stdin.readline

# 유레카 수 저장
eurka_nums = []
for i in range(1, 46):
    eurka_nums.append(i * (i + 1) // 2)

n = int(input())

for _ in range(n):
    num = int(input())
    check = False  # 각 테스트 케이스마다 check 변수 초기화

    for i in range(len(eurka_nums)):
        for j in range(i, len(eurka_nums)):
            for k in range(j, len(eurka_nums)):
                if num == eurka_nums[i] + eurka_nums[j] + eurka_nums[k]:
                    check = True
                    break
            if check:
                break
        if check:
            break

    if check:
        print(1)
    else:
        print(0)