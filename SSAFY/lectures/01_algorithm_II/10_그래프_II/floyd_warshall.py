def floyd_warshall():
    for i in range(V):
        for j in range(V):
            if i == j:              # 내 위치로는 이동 불가능 하므로 0으로 초기화
                dist[i][j] = 0
            elif graph[i][j] == 0:  # 인접 행렬 상으로 이동 할 수 없다고 표기 된 부분은
                dist[i][j] = 1e9   # 각 노드에서 이동 가능한 정보들을 담을 것이므로 충분히 큰 수로 초기화
            else:
                dist[i][j] = graph[i][j]    # 그 외에는 가중치 정보

    for k in range(V):              # 중간 노드 : 거쳐가는 길
        for i in range(V):          # 출발 노드
            for j in range(V):      # 도착 노드
                '''
                    dist[i][j] : 출발 노드에서 도착노드로 직접 갈 수 있을 때의 비용
                    dist[i][k] + dist[k][j] 는 중간 노드를 거쳐서 도착노드로 가는 거리
                    둘 중 더 싼 가격을 dist에 삽입.
                '''
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

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

# 중간노드를 거쳐 가는게 더 싼경우를 확인하기
# edge = [
#     [0, 1, 1],
#     [0, 2, 31],
#     [0, 5, 60],
#     [0, 6, 51],
#     [1, 2, 1],
#     [2, 4, 1],
#     [2, 6, 25],
#     [3, 4, 34],
#     [3, 5, 18],
#     [4, 5, 1],
#     [4, 6, 51],
# ]

# 인접 행렬 방식으로 그래프 생성
graph = [[0] * V for _ in range(V)]

for x, y, weight in edge:
    graph[x][y] = weight
    graph[y][x] = weight  # 무방향 그래프

# 거리 배열 초기화
dist = [[1e9] * V for _ in range(V)]

# 플로이드-워샬 알고리즘 실행
floyd_warshall()

# 모든 노드 쌍 간의 최단 거리 출력
for i in range(V):
    for j in range(V):
        if dist[i][j] == 1e9:
            print("INF", end=' ')
        else:
            print(dist[i][j], end=' ')
    print()
