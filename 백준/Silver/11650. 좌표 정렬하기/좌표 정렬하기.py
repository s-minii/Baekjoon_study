# 11650 : OX 좌표 정렬하기
# 해결 방법
# 값을 받아 저장해두고, sort를 이용하여 x가 작은 순서, y가 작은 순서로 정렬하여 출력한다.

cnt = int(input())

array = []

for i in range(cnt):
    array.append(list(map(int, input().split())))

    #sort와 sorted의 차이 : sort는 리스트만, sorted는 반복 가능한 모든 작업에 사용 가능
array.sort()

for j in array:
    print(j[0], j[1])