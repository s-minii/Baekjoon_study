# 1755 : 숫자놀이

import sys
input = sys.stdin.readline

word = { "0" : "zero", "1" : "oen" , "2" : "two" , "3" : "three" , "4" : "four" ,
         "5" : "five",  "6" : "six", "7" : "seven" , "8" : "eight" , "9" : "nine" }
n, m = map(int, input().split())
num = []

for i in range(n, m + 1):
    temp = []
    for j in str(i):
        temp.append([word[j], j])
    num.append(temp)

num.sort()

for k in range(len(num)):
    res = ""

    if k % 10 == 0 and k != 0:
        print()

    for a, b in num[k]:
        res += b
    print(res, end=" ")