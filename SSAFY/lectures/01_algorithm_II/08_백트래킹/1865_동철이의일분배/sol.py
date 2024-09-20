import sys
sys.stdin = open('input.txt')

def search(now, acc):
    global result
    if result >= acc: return

    if now == N:
        result = max(result, acc)   # 최댓값 갱신
        return
    else:
        for w in range(N):
            if not visited[w]:
                visited[w] = 1
                # 확률 계산을 위해 원본 값에서 100을 나눈 값을 곱셈
                search(now+1, acc * (data[now][w] / 100))
                visited[w] = 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    visited = [0] * N
    search(0, 1)
    print(f'#{tc} {result*100:6f}')