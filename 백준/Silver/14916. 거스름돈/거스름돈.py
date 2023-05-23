# 14916 : 거스름돈
# 풀이 : 그리디 알고리즘 (5번 이상 틀리고, 새로운 해답이 생각나질 않아 답을 참고했다,, ㅎ)
# 참고 : https://esoongan.tistory.com/56

n = int(input())
cnt = 0

while True:
    if n % 5 == 0:
        cnt += n//5
        break
        
    else:
        # 5의배수가 아니면 2씩 빼면서 5의 배수가 나오도록 한다.
        n -= 2
        cnt += 1

    if n < 0:
        break

if n < 0:
    print(-1)
else:
    print(cnt)