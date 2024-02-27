import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
data = list(map(int, input().rstrip().split()))

# 누적 합 딕셔너리
# list의 index로 접근하려고 하면 index길이가 최대 20억이 되어야됨
sum_dict = {0: 1}

sum_ = 0
answer = 0

for i in data:
    sum_ += i

    # 현재까지 누적합 중에서 누적합 - (이전 누적합) = k 가 있으면
    # 즉 누적합 - k값이 이전에 나왔으면 정답개수 추가
    if sum_ - k in sum_dict.keys():
        answer += sum_dict[sum_ - k]

    # 누적 합 딕셔너리 갱신
    sum_dict[sum_] = sum_dict.get(sum_, 0) + 1

print(answer)