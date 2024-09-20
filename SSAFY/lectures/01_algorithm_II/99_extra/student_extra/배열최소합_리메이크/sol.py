import sys
sys.stdin = open('input.txt')

def search(r, cnt):
    global result

    if result < cnt:
        return
    if r == N:
        if result > cnt:
            result = cnt
    else:
        for k in range(N):
            if visited[k] <= 2:
                visited[k] += 1
                search(r+1, cnt + data[r][k])
                visited[k] -= 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result = N * 101
    search(0, 0)
    print(f'#{tc} {result}')