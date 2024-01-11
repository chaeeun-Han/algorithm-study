n, m = map(int, input().split())
dna = [input() for _ in range(n)]
sum = 0
result = ''

for i in range(m):
    a, c, g, t = 0, 0, 0, 0
    for j in range(n):
        if dna[j][i] == 'T':
            t += 1
        elif dna[j][i] == 'A':
            a += 1
        elif dna[j][i] == 'G':
            g += 1
        else:
            c += 1

    if max(a, c, g, t) == a:
        result += 'A'
    elif max(a, c, g, t) == c:
        result += 'C'
    elif max(a, c, g, t) == g:
        result += 'G'
    elif max(a, c, g, t) == t:
        result += 'T'

    sum += n - max(a, c, g, t)

print(result)
print(sum)