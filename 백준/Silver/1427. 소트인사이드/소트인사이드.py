n = input()
data = [int(i) for i in n]

for i in range(1, len(data)):
    for j in range(i, 0, -1):
        if data[j] > data[j-1]:
            data[j], data[j-1] = data[j-1], data[j]
        else:
            break

for i in data:
    print(i, end='')