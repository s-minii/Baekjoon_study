# 1927 번 : 최소 힙
# 풀이 : 힙 라이브러리를 사용하지 않고, 문제를 해결하고자 하였다.
# 풀이 방법은 이해했지만 구현하지 못하였고, 풀이를 참고하여 문제를 해결하였다.
# 참고 :https://claude-u.tistory.com/153

import sys
import heapq

input = sys.stdin.readline

cnt = int(input())
heap = []

for _ in range(cnt):
    num = int(input())
    if num != 0:
        heapq.heappush(heap, num)
    else:
        # try-except : 오류처리를 위해 사용
        # try : 실행할 코드
        try:
            print(heapq.heappop(heap))
        # 예외 처리 코드
        except:
            print(0)