# 1966번 : 프린터 큐
# 분류 : 구현, 자료 구조, 시뮬레이션, 큐
# 참고 : https://ywtechit.tistory.com/184

import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    N, M = map(int, input().split())
    importance = list(map(int, input().split())) #중요도

    index= [i for i in range(N)]
    index[M] = 'target'
    cnt = 0

    while importance:
        if importance[0] == max(importance):
            cnt +=1
            if index[0] == 'target':
                print(cnt)
                break
            importance.pop(0)
            index.pop(0)
        else:
            importance.append(importance.pop(0))
            index.append(index.pop(0))


