import sys
sys.stdin = open('input.txt')

from heapq import heappop, heappush

def spanning_tree():
    tree=[]
    min_heap = [(0,1)]  # 시작 노드를 포함한 최소 힙 생성
    result = 0  # 최소 스패닝 트리의 가중치 합을 저장할 변수 초기화
    while min_heap:
        weight, now = heappop(min_heap)  # 현재 가장 가까운 노드와 해당 노드까지의 가중치를 가져옴
        if not visited[now]:  # 해당 노드가 방문되지 않은 경우에만 실행
            visited[now] = 1  # 해당 노드를 방문했음을 표시
            tree.append([weight,now])
            result += weight  # 현재 노드까지의 가중치를 결과에 더함
            for next_weight, next_node in graph[now]:  # 현재 노드와 연결된 모든 노드에 대해 반복
                if not visited[next_node]:  # 연결된 노드가 방문되지 않은 경우에만 실행
                    heappush(min_heap, (next_weight, next_node))  # 다음 노드와 해당 노드까지의 가중치를 최소 힙에 추가
            print(tree)
    return result  # 최소 스패닝 트리의 가중치 합 반환

for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())  # 노드의 개수 V와 간선의 개수 E 입력
    graph = [[] for _ in range(E)]  # 그래프 생성
    visited = [0] * (V + 1)  # 방문 여부를 저장할 리스트 초기화
    for _ in range(E):
        s, e, w = map(int, input().split())  # 간선 정보 입력
        graph[s].append([w, e])  # 시작 노드와 도착 노드, 가중치 추가
        graph[e].append([w, s])  # 시작 노드와 도착 노드, 가중치 추가 (양방향 그래프)
    print(f'#{tc} {spanning_tree()}')  # 결과 출력