import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
data = []

for i in range(N):
    data.append(input().lower())

for idx, word in enumerate(data):
    if word == word[::-1]:
        print(f"#{idx + 1} YES")
    else:
        print(f"#{idx + 1} NO")