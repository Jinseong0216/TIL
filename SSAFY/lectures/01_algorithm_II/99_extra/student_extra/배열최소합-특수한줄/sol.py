import sys
sys.stdin = open("input.txt")


def search(r, cnt, arr):
    global result
    if result < cnt:
        return

    if r == N:
        if result > cnt:
            print(arr)
            result = cnt
    else:
        for k in range(N):
            if r + 1 in special:
                search(r + 1, cnt + data[r][k], arr + [data[r][k]])
            elif not visited[k]:
                visited[k] = 1
                search(r + 1, cnt + data[r][k], arr + [data[r][k]])
                visited[k] = 0


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    special = list(map(int, input().split()))
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result = N*11
    search(0, 0, [])
    print(f'#{tc} {result}')