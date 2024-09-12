for t in range(1, 1+int(input())):
    length = int(input())
    arr = list(map(int, input().split()))
    print(f'#{t}', abs(arr.index(min(arr)) - (length - 1 - arr[::-1].index(max(arr)))))