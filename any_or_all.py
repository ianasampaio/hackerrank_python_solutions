N,arr = int(input()),input().split()
print(any([num == num[::-1] for num in arr if all([int(n) > 0 for n in arr])]))
