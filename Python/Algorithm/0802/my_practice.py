for t in range(1, int(input())+1):
    arr = input().replace('()', '1')
    N = len(arr)
    temp = [0]*N
    lst = []

    total = 0
    for i in range(len(arr)):
        if arr[i] == '1':
            temp[i] = 1
        elif arr[i] == '(':
            lst += [i]
        else:
            total += (sum(temp[lst.pop():i]) + 1)
    print(f'#{t} {total}')
