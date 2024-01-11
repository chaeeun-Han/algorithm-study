a = int(input())
t = int(input())
b = int(input())
cnt = 0

word = [0, 1, 0, 1, 0, 0, 1, 1]
ans = [0, 1, 0, 1, 0, 0, 1, 1]

# t번째 b를 찾지 못한 동안
while ans.count(b) < t:
    word.insert(4, 0)
    word.append(1)
    for i in word:
        ans.append(i)

for i in range(len(ans)):
    if b == ans[i]:
        cnt += 1
    if cnt == t:
        print(i % a)
        break