# 1018번 : 체스판 다시 칠하기
# 종류 : 브루트포스 알고리즘
# 참고 : https://ittrue.tistory.com/60

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
result = []

for _ in range(n):
    arr.append(input())

# 8X8 체스판
for i in range(n-7):
    for j in range(m-7):
        white_index = 0
        black_index = 0

        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if arr[a][b] != 'B':
                        white_index += 1

                    if arr[a][b] != 'W':
                        black_index += 1
                else:
                    if arr[a][b] != 'W':
                        white_index += 1

                    if arr[a][b] != 'B':
                        black_index += 1

        result.append(white_index)
        result.append(black_index)

print(min(result))