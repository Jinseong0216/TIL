import heapq

def prim(start):
    # 가중치가 가장 낮은 값들 우선 탐색 대상으로 활용
    q = []
    # 최소 신장 트리에 포함되었는지 확인 할 배열
    visited = [0] * V

    # 최소 비용 합계
    result = 0

    # 가중치, 정점 정보. : 시작 노드이기때문에 가중치 0으로 시작,
    # 최소힙 구성의 비교 대상이 가중치이므로, 가중치 우선 삽입
    heapq.heappush(q, (0, start))

    while q:
        # 현재 조사 대상 처리
        weight, now = heapq.heappop(q)
        if not visited[now]:            # 아무도 방문한 적 없을때 만
            print(now)
            visited[now] = 1            # 아니라면 방문 표시 후
            result += weight            # 가중치 추가
            for next in range(V):       # 모든 노드에 대해서
                # 간선이 존재하고 방문한 적 없는 대상에 대해서
                if graph[now][next] and not visited[next]:
                    # 힙에 값 삽입.
                    heapq.heappush(q, (graph[now][next], next))

    return result

# 노드의 개수, 간선의 개수를 입력받기
V, E = 7, 11
edge = [
    [0, 1, 32],
    [0, 2, 31],
    [0, 5, 60],
    [0, 6, 51],
    [1, 2, 21],
    [2, 4, 46],
    [2, 6, 25],
    [3, 4, 34],
    [3, 5, 18],
    [4, 5, 40],
    [4, 6, 51],
]

# 인접 행렬 방식
graph = [[0] * (V) for _ in range(V)]

# 가중치 있는 무방향 그래프
for idx in range(E):
    x, y, weight = edge[idx]
    graph[x][y] = weight
    graph[y][x] = weight

for g in graph:
    print(g)

result = prim(0)

print(result)