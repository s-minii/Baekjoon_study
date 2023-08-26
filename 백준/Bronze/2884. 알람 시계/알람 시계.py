# 2884번 : 알람 시계
# 분류 : 수학, 사칙연산

import sys
input = sys.stdin.readline

H, M = map(int, input().split())

M -= 45

if M >= 0:
    print(H, M)

elif H>=1 and M<=0:
    print(H-1, M+60)

elif H==0 and M<=0:
    print(23, M+60)