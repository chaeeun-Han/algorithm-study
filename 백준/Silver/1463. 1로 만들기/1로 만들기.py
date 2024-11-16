# 3, 2로 나누어 떨어지면 나누기 OR 1 빼기
# 연산 3개를 적절히 사용해서 1을 만드는 연산의 최소 횟수

x = int(input())
cnt_list = [0] * 1000001

# 바텀업
for i in range(2, x+1):
    # 1 빼기
    cnt_list[i] = cnt_list[i-1] + 1
    # 2로 나누기
    if (i % 2 == 0):
        cnt_list[i] = min(cnt_list[i], cnt_list[i//2] + 1)
    # 3으로 나누기
    if (i % 3 == 0):
        cnt_list[i] = min(cnt_list[i], cnt_list[i//3] + 1)

print(cnt_list[x])