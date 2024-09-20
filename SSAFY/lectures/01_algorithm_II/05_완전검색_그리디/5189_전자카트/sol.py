import sys
sys.stdin = open('input.txt')

def search(r, n, cnt):
    global result
    if result < cnt:    # 현재까지 누적값이 이미 최솟값을 초과했다면
        return          # 더 이상 조사하는 의미 없음. 조사 종료.

    if r == N:          # 모든 장소에 방문했다면
        cnt += data[n][0]   # 마지막으로 0번으로 돌아가고,
        if result >= cnt:   # 그 값이 최솟값이면
            result = cnt    # 최솟값 갱신
    else:
        for w in range(1, N):   # 0번을 제외한 장소에 대해
            if n != w and not visited[w]:   # 동일 장소가 아니고, 방문한 적 없는 곳이라면
                visited[w] = 1              # 방문 표시 후
                search(r+1, w, cnt + data[n][w])    # 해당 위치로 조사 시작
                visited[w] = 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result = sum(sum(data, [])) # 충분히 큰 값

    search(1, 0, 0)             # 항상 0번에서 출발
    print(f'#{tc} {result}')

