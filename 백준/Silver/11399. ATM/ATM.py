# 11399 : ATM

cnt = int(input())
p = list(map(int, input().split()))
p.sort()

result = 0
for i in range(cnt):
    if i != 0:
        p[i] = p[i] + p[i-1]
        result += p[i]
    else:
        result += p[0]

print(result)