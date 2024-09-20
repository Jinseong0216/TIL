import sys
sys.stdin = open('algo1_sample_in.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())    # 구역 수 N, 이동거리 K
    arr = [0] + list(map(int, input().split())) # 구역별 먹이

    last = 1    # 마지막으로 먹이를 먹은 곳
    ans = N
    while last + K < N:     # 마지막 칸에 도착 못하면
        next = last               # 다음에 먹이를 먹을 곳
        for i in range(last+1, last+K+1):   # 먹이를 먹으러 이동
            if arr[i]:      # 먹이가 있으면
                next = i
        if next == last:        # 먹이를 먹는데 실패한 경우
            ans = last + K
            break
        last = next
    print(f'#{tc} {ans}')
