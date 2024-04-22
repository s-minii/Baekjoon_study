import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
grid = []
max_sum = 0

for _ in range(N):
    row = list(map(int, input().split()))
    grid.append(row)


# 각 행의 합 계산
for i in range(N):
    row_sum = sum(grid[i])
    if row_sum > max_sum:
        max_sum = row_sum

# 각 열의 합 계산
for i in range(N):
    col_sum = 0
    for j in range(N):
        col_sum += grid[j][i]
    if col_sum > max_sum:
        max_sum = col_sum

# 두 대각선의 합 계산
left_diagonal_sum = 0
right_diagonal_sum = 0
for i in range(N):
    left_diagonal_sum += grid[i][i]
    right_diagonal_sum += grid[i][N-i-1]

# 대각선 합 중 최대값
max_sum = max(max_sum, left_diagonal_sum, right_diagonal_sum)

print(max_sum)