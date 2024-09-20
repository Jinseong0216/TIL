def bellman_ford(start):
    # 시작 노드의 최단 거리 0으로 설정
    distance[start] = 0

    # V-1번 반복
    for i in range(V - 1):
        for x, y, weight in new_edge:
            if distance[x] != 1e9 and distance[x] + weight < distance[y]:
                distance[y] = distance[x] + weight

    # 음수 사이클 확인
    for x, y, weight in new_edge:
        if distance[x] != 1e9 and distance[x] + weight < distance[y]:
            return False

    return True


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

# 음수 가중치가 있다면 테스트
# edge = [
#     [0, 1, -1],
#     [0, 2, 31],
#     [0, 5, 60],
#     [0, 6, 51],
#     [1, 2, 21],
#     [2, 4, 46],
#     [2, 6, 25],
#     [3, 4, 34],
#     [3, 5, 18],
#     [4, 5, 40],
#     [4, 6, 51],
# ]

# 양방향 간선 추가
new_edge = []
for x, y, weight in edge:
    new_edge.append([x, y, weight])  # 원래 간선
    new_edge.append([y, x, weight])  # 무방향 그래프


# 거리 배열 무한대로 초기화
distance = [1e9] * V

# 벨만-포드 알고리즘 실행 (0번 노드에서 시작)
if bellman_ford(0):
    # 모든 노드로 가기 위한 최단 거리 출력
    for i in range(V):
        if distance[i] == 1e9:
            print("INF", end=' ')
        else:
            print(distance[i], end=' ')
