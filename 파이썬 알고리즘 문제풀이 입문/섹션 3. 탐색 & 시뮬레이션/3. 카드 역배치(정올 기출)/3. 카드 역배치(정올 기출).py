import sys
sys.stdin = open("input.txt", "rt")


card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for _ in range(10):
    a, b = map(int, input().split())
    for i in range((b-a+1)//2):
        card[a-1+i], card[b-1-i] = card[b-1-i], card[a-1+i]

print(*card)