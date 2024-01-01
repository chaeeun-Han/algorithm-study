n = int(input())
drink = list(map(int, input().split()))
drink.sort()
sum = drink[-1]

for i in range(len(drink) - 1):
    sum += drink[i] / 2

print(sum)