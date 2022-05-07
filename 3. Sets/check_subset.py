for _ in range(int(input())):
    n_a = int(input())
    a = set(map(int, input().split()))

    n_b = int(input())
    b = set(map(int, input().split()))

    print(a.issubset(b))
