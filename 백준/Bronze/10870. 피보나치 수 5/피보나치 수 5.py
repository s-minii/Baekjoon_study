# 10870 : 피보나치 수 5

cnt = int(input())
num_0 = 0
num_1 = 1
num_2 = 1

if cnt == 0:
    print(0)
elif cnt == 1:
    print(1)
elif cnt >= 2:
    for i in range(cnt):
        num_0 = num_1
        num_1 = num_2
        num_2 = num_0 + num_1
    print(num_0)