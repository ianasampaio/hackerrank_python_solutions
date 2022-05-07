a = set(map(int, input().split()))
is_superset = []

for _ in range(int(input())):
    b = set(map(int, input().split()))
    if a.issuperset(b):
        is_superset.append(True)
    else:
        is_superset.append(False)

print(all(is_superset))