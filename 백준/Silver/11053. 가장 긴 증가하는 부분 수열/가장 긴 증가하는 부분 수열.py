# 11053번 : 가장 긴 증가하는 부분 수열 (LIS)
# 종류 : 다이나믹 프로그래밍
# 참고1 : https://techblog-history-younghunjo1.tistory.com/295
# 참고2 : https://chanhuiseok.github.io/posts/algo-49/

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

#DP 테이블로 1로 초기화
dp = [1] * n

# 앞 순서의 모든 원소에서 끝나는 최장 수열들의 길이 중, 가장 긴 것을 골라서 +1
for i in range(1, n):
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)

result = max(dp)
print(result)