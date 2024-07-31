T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = max(arr) - min(arr)

    print(f'#{t}', ans)


for t in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    
    max_value, min_value = arr[0], arr[0]

    for i in range(1, N):
        if max_value < arr[i]: max_value = arr[i]
        if min_value > arr[i]: min_value = arr[i]

    ans = max_value - min_value
    print(f'#{t}', ans)