n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    v = list(input().split())

    if v[0] == 'remove':
        s.remove(int(v[1]))
    elif v[0] == 'discard':
        s.discard(int(v[1]))
    elif v[0] == 'pop':
        s.pop()
print(sum(s))