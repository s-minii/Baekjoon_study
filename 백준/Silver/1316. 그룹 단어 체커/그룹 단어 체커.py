# 1316번 : 그룹 단어 체커
# 풀이 : # 모두 그룹 단어라고 생각한 뒤, 아닌 것들을 제거하는 방식
n = int(input())
cnt = n

for i in range(n):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            continue
            
        elif word[j] in word[j+1:]:
            cnt -= 1
            break

print(cnt)
