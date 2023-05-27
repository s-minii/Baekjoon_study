#1541번 : 잃어버린 괄호 (그리디 알고리즘)

arr = input().split('-')
num = []

for i in arr:
    sum = 0
    n = i.split('+')

    for j in n:
        sum += int(j)
    num.append(sum)

k = num[0]

for i in range(1, len(num)):
    k -= num[i]
print(k)