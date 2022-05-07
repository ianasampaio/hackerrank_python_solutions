n = int(input())
a = set(map(int, input().split()))

for _ in range(int(input())):
    v,_ = input().split()
    w = set(map(int, input().split()))

    if v == 'intersection_update':
        a.intersection_update(w)
    elif v == 'update':
        a.update(w)
    elif v == 'difference_update':
        a.difference_update(w)
    elif v == 'symmetric_difference_update':
        a.symmetric_difference_update(w)
print(sum(a))