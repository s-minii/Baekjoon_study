# 1783번 : 병든 나이트 (그리디 알고리즘 연습)

n, m = map(int, input().split())

# 체스판 세로 길이가 1인 경우
if n == 1:
    print(1)
    
# 체스판의 세로 길이가 2인 경우, 최대 4칸을 방문할 수 있다.
elif n == 2:
    # m // 2는 오른쪽으로 이동하는 횟수
    print(min(4, (m+1) //2))

# 체스판의 세로 길이가 3 이상, 가로 길이가 6 이하인 경우
else:
    if m <= 6:
        print(min(4, m))

    else:
        print(m-2)