money = 1000 - int(input())
cnt = 0

array = [500, 100, 50, 10, 5, 1]

for coin in array:
    cnt += money // coin
    money %= coin

print(cnt)