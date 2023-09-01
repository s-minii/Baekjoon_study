# 15829번 : Hashing
# 분류 : 구현, 문자열, 해싱
# 참고 : https://claude-u.tistory.com/432

import sys
input = sys.stdin.readline

n = int(input())
str = input()
result = 0

# ord : 아스키 코드 값을 돌려준다.
for i in range(n):
    result += (ord(str[i])-96) * (31 ** i)
print(result % 1234567891)