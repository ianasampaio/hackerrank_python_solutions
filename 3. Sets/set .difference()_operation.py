n_eng = int(input())
s_eng = set(map(int, input().split()))

n_french = int(input())
s_french = set(map(int, input().split()))

print(len(s_eng - s_french))