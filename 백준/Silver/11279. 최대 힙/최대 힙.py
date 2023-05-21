# 11279 : 최대 힙

import sys
import heapq

input = sys.stdin.readline

cnt = int(input())
heap = []

for _ in range(cnt):
    num = int(input())
    if num :
        heapq.heappush(heap, (-num, num))

    else:
        if len(heap) >=1 :
            print(heapq.heappop(heap)[1])
        else:
            print(0)