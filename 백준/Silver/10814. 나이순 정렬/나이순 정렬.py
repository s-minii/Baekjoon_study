# 10814 : 나이순 정렬
# 나이와 이름이 공백으로 주어진다.
# 나이 순, 가입한 순으로 나이와 이름을 공백으로 구분하여 출력
# 참고 : https://velog.io/@1204jh/10814

count = int(input())

arr = []

#값을 입력받아 리스트에 저장 (공백으로 구분)
for i in range(count):
    age, name = map(str, input().split())
    age = int(age)
    arr.append((age, name))

#arr의 요소 중 첫 번째 요소만 추출하여 비교 대상으로 정렬한다.
arr.sort(key=lambda x: x[0])

#출력
for i in arr:
    print(i[0], i[1])