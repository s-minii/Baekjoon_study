# 11047번 : 동전 0
# 풀이 : 문제에 오름차순으로 동전의 가치를 준다고 하였다.
# 그래서 제일 큰 가치의 동전부터 coin이 나누어 지는 값들을 순서로 나누며 카운팅한다.

import sys
input = sys.stdin.readline

cnt, coin = map(int, input().split())
coinType = []

for i in range(cnt):
    coinType.append(int(input()))

coinType = sorted(coinType, reverse=True)

result = 0

def coinDivide(coin, coinType):
    return coin // coinType

for i in range(cnt):
    if coinType[i] > coin:
        continue

    count = coinDivide(coin, coinType[i])  # 나눈 개수를 변수에 저장
    result += count
    coin -= count * coinType[i]  # 나눈 만큼 값을 감소시킴

print(result)