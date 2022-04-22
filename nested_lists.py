if __name__ == '__main__':
    n = int(input())
    arr = [[input(), float(input())] for _ in range(n)]

    score = sorted([arr[c][1] for c in range(0,len(arr))])

    c = 0
    for _ in score:
        if score[c] == score[c+1]:
            c=c+1
        else:
            c=c+1
            break

    result = score[c]

    names = sorted([arr[y][0] for y in range(0,len(arr)) if arr[y][1] == result])

    for n in names:
        print(n)
