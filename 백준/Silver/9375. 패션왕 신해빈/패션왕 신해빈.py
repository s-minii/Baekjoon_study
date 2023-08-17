# 9375번 : 패션왕 신해빈
# 분류 : 수학, 자료구조, 조합론, 해시를 사용한 집합과 맵
# 참고 : https://hongcoding.tistory.com/60

import sys
input = sys.stdin.readline

cnt = int(input())

for i in range(cnt):
    top = int(input())
    clothes = {}

    for j in range(top):
        top_key, top_value = input().split()

        if top_value not in clothes.keys():
            clothes[top_value] = 1
        else:
            clothes[top_value] +=1


    #각 종류별 항목의 개수
    result = 1

    for k in clothes:
        result *= (clothes[k]+1)

    # 알몸인 경우 제외
    print(result-1)