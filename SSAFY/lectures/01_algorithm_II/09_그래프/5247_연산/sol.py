import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0] * 1000001     # 연산 도중에도 100만까지만 연산
    queue = deque([N])          # 조사 시작 대상 N 삽입

    while visited[M] == 0:      # 목표 숫자에 도달한 적이 있는지 체크
        now = queue.popleft()
        # 현재 숫자에서 가능한 연산을 수행하여 새로운 숫자 생성
        for i in [now+1, now-1, now*2, now-10]:
            # 숫자가 연산 범위 100만 이내에 있고 방문하지 않았다면
            if 0 < i <= 1000000 and visited[i] == 0:
                visited[i] = visited[now] + 1           # 연산 횟수 표시
                queue.append(i)                         # 해당 연산 결과를 다시 다음 조사대상으로 삽입

    # 조사 완료 후, 목표 지점에 기록된 연산 횟수 출력
    print(f'#{tc} {visited[M]}')