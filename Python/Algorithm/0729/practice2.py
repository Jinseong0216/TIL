T = int(input())

for t in range(1, T+1):
    N = int(input())
    boxes = list(map(int, input().split()))

    max_distance = 0

    for i in range(N):
        cnt = 0
        for j in range(i+1, N):
            if boxes[i] <= boxes[j]:
                cnt += 1
        max_distance = max(max_distance, N - 1 - i - cnt)

    print(f'#{t}', max_distance)