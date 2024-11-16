# [1로 만들기] 난이도 1.5/3, 풀이 시간 20분, 시간 제한 1초, 메모리 제한 128MB
# 5, 3, 2로 나누어 떨어지면 나누기 OR 1 빼기
# 연산 4개를 적절히 사용해서 1을 만드는 연산의 최소 횟수

x = int(input())
# 1<=x<=30,000 조건에 의거하여 dp테이블 생성
cnt_list = [0] * 30001

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
    # 5로 나누기
    if (i % 5 == 0):
        cnt_list[i] = min(cnt_list[i], cnt_list[i//5] + 1)


print(cnt_list[x])
