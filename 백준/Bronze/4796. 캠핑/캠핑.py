li = []
while True:
    temp_li = [int(i) for i in input().split()]
    if temp_li[0]==0 and temp_li[1] == 0 and temp_li[2] == 0: break
    li.append(temp_li)
for i, (l, p, v) in enumerate(li):
    if v % p <= l:
        print(f"Case {i+1}: {(v//p)*l+v%p}")
    else:
        print(f"Case {i+1}: {(v//p)*l+l}")