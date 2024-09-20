import sys
sys.stdin = open('input.txt')

#     우 하 로만 이동 가능
dx = [0, 1]
dy = [1, 0]

# 좌표, 누적치
def DFS(x, y, cnt):
    for k in range(2):  # 우, 하로만 이동가능하므로 k는 0, 1
        nx, ny = x + dx[k], y + dy[k]
        # 다음 조사 대상이 범위를 넘어서지 않고, 현재 누적치가 최소인 경우에만
        if nx < N and ny < N and visited[nx][ny] >= cnt + data[nx][ny]:
            visited[nx][ny] = cnt + data[nx][ny]    # 누적치 갱신 후,
            DFS(nx, ny, cnt + data[nx][ny])  # 다음 조사대상으로 삽입


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    result = sum(sum(data, []))     # 충분히 큰 값
    visited = [[result] * N for _ in range(N)]  # 충분히 큰 값으로, 누적치 초기화
    DFS(0, 0, data[0][0])
    result = visited[N-1][N-1]  # 최종 도착지점의 값을 출력
    print(f'#{tc} {result}')
