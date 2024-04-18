import sys
sys.stdin = open("input.txt", "rt")

N = input()
numbers = ""
cnt = 0

for i in N:
    if i.isdigit():
        numbers += i

numbers = str(int(numbers))
print(numbers)

numbers = int(numbers)

for i in range(1, numbers+1):
    if numbers % i == 0:
        cnt += 1

print(cnt)