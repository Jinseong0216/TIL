import sys
sys.stdin = open('input.txt')

from collections import deque

def search():
    q = deque()
    for i in range(N):
        if in_degree[i] == 0:
            q.append(i)

    # 최종 목표는 최소 학기
    # 모든 과목을 완료 했는지 알기 위해서는
    completed = 0   # 완료된 과목이 몇개냐 비교용
    semster = 0     # 총 소요된 학기는?

    while q:        # 조사 대상이 남아 있는 동안
        semster += 1
        # 현재 학기에 삽입된 모든 진입차수가 0인 과목들 제거
        for _ in range(len(q)):
            current = q.popleft()
            completed += 1          # 과목 완료

            for next in graph[current]:
                in_degree[next] -= 1
                if in_degree[next] == 0:
                    q.append(next)

    if completed == N:      # 전체 과목에 대해서 처리 완료
        return semster
    else:
        return -1


T = int(input())  # 테스트 케이스 수
for tc in range(1, T + 1):
    N = int(input())  # 과목의 개수
    # 첫 번째 숫자는 선수 과목의 개수이므로 제외
    pre = [list(map(int, input().split()))[1:] for _ in range(N)]

    # 인접 행렬로 만들 수도 있는데..
    # 공간이랑, 시간 생각해서... 인접 리스트로 만들자.
    graph = [[] for _ in range(N)]
    in_degree = [0] * N     # 진입 차수 정보 초기화

    # 그래프 구성과 진입 차수 정보 갱신
    for i in range(N):
        prereq = pre[i]
        for p in prereq:
            # 선수 과목 -> 현재 과목으로 갈 수 있음을 인접 리스트에 표기
            graph[p - 1].append(i)
            # 해당 현재 과목의 진입차수 개수 + 1
            in_degree[i] += 1

    # print(graph, in_degree)
    result = search()
    print(f'#{tc} {result}')







