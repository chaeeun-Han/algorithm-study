n = int(input())
data = []

for i in range(n):
    data.append(int(input()))

data.sort(reverse=True)
maxWeight = data[0]

for i in range(n):
    if (maxWeight < data[i] * (i + 1)):
        maxWeight = data[i] * (i + 1)

print(maxWeight)