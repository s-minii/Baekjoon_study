# 2309 : 일곱난쟁이
# 참고 : https://ji-gwang.tistory.com/244

import sys
input = sys.stdin.readline

hap = 100
nan = []

for i in range(9):
    nan.append(int(input()))

nan.sort()
sum_nan = sum(nan)


for i in range(len(nan)):
    for j in range(i+1, len(nan)):
        if sum_nan - nan[i] - nan[j] == 100:
            for k in range(len(nan)):
                if k == i or k == j:
                    pass
                else :
                    print(nan[k])
            exit()