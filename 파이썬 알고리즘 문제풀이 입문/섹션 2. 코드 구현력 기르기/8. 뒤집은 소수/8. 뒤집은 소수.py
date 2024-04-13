import sys
sys.stdin = open("input.txt", "rt")

N = int(input())

def reverse(x):
    res = 0
    while x > 0:
        t = x % 10
        res = res*10+t
        x=x//10
    return res

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x//2+1):
        if x%i==0:
            return False
    else:
        return True

arr = list(map(int, input().split()))
result = []

for x in arr:
    reversed_x = reverse(x)
    if isPrime(reversed_x):
        result.append(reversed_x)

for num in result:
    print(num, end = ' ')