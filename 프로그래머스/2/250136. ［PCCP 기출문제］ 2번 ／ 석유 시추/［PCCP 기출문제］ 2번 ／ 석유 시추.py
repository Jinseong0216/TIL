from collections import deque

def solution(land):
    N, M = len(land), len(land[0])
    column_info = [0] * M  # 각 열의 최대 석유량을 저장할 리스트

    # BFS로 각 석유 덩어리의 면적 계산 및 포함 열 누적 업데이트
    def bfs(start_i, start_j):
        queue = deque([(start_i, start_j)])
        land[start_i][start_j] = 0  # 방문 처리
        area = 1  # 현재 덩어리의 면적
        columns_visited = set([start_j])  # 현재 덩어리가 포함된 열 집합

        # 인접한 석유 구역 탐색
        while queue:
            i, j = queue.popleft()
            for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                n_idx, n_jdx = i + di, j + dj
                if 0 <= n_idx < N and 0 <= n_jdx < M and land[n_idx][n_jdx] == 1:
                    land[n_idx][n_jdx] = 0  # 방문 처리
                    queue.append((n_idx, n_jdx))
                    area += 1
                    columns_visited.add(n_jdx)

        # 방문한 열에 대해 석유 덩어리 면적을 누적합
        for j in columns_visited:
            column_info[j] += area

    # 각 좌표에 대해 BFS 실행
    for i in range(N):
        for j in range(M):
            if land[i][j] == 1:  # 기름이 있는 경우만 BFS 실행
                bfs(i, j)

    return max(column_info)  # 가장 큰 석유량 반환
