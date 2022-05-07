n = int(input())
a = list(map(int, input().split()))

b = set()
c = set()

for i in range(len(a)):
    if a[i] not in b:
        b.add(a[i])
    else:
        c.add(a[i])
print(*(b-c))
