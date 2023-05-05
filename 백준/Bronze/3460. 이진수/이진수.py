# 3460 : 이진수
# bin_n[-j-1]을 한 이유 : 2진수 값의 역순을 확인해야 하기 때문에

cnt = int(input())

for i in range(cnt):
    n = int(input())
    bin_n = bin(n)

    for j in range(len(bin_n[2:])):
        if bin_n[-j-1] == '1':
            print(j, end = ' ')