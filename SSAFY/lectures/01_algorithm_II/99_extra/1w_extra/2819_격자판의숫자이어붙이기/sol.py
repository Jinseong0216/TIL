import sys
sys.stdin = open('input.txt')

from collections import deque
#      상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def search(x, y):
    #           0, 0, 1, '1'
    q = deque([(x, y, 1, data[x][y])])  # 시작지점의 문자열과 함께 시작
    while q:
        x, y, cnt, word = q.popleft()
        if cnt == 7:            # 총 7글자가 되었다면.
            result.add(word)    # 결과에 만들어진 문자열 주가
            continue            # 다음 조사 작업 시작하지 않음.

        for k in range(4):      # 내 방향에 대해서
            nx = x + dx[k]
            ny = y + dy[k]
            # 범위를 벗어나지 않고, 아직 문자열이 7글자가 안됐다면
            if 0 <= nx < 4 and 0 <= ny < 4 and cnt <= 6:
                q.append((nx, ny, cnt+1, word + data[nx][ny]))  # 문자열추가가

T = int(iput())

for tc in range(1, T+1):
    data = [list(input().split()) for _ in range(4)]
    result = set()      # 중복을 제거한 결과를 담을 result

    # 전수 조사
    for i in range(4):
        for j in range(4):
            search(i, j)
    print(f'#{tc} {len(result)}')