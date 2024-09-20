# 기본적인 최소비용로직에다 값의 차이만큼 추가.
import sys
sys.stdin = open('input.txt')
from heapq import heappush, heappop

def dijkstra(start):
  pq = []
  # 시작점의 weight, node 번호를 한 번에 저장
  heappush(pq, (0,start))
  # 시작노드 초기화
  distance[start] = 0
  while pq:
    # 최단거리노드에 대한 정보
    dist,now = heappop(pq)
    # pq의 특성때문에 더 긴거리가 미리 저장되어 있음
    #  now가 이미 처리된 노드라면 pass
    if distance[now] < dist:
      continue
    # now에서 인접한 다른 노드 확인
    for to in graph[now]:
      next_dist = to[0]
      next_node = to[1]

      # 누적거리계산
      new_dist = dist + next_dist

      # 이미 더 짧은 거리로 간 경우 pass
      if new_dist >= distance[next_node]:
        continue
      distance[next_node] = new_dist
      # 누적거리를 최단거리로 갱신
      heappush(pq,(new_dist,next_node)) #next_node의 인접노드들을 pq에 추가
  print(f'#{tc} {distance[-1]}')
  
T = int(input())
for tc in range(1,T+1):
    INF = int(1e9)
    start = 0  # 시작 노드 번호



    N = int(input())
    V,E= N*N,N*N
    matrix = [list(map(int,input().split())) for _ in range(N)]

    graph = [[] for _ in range(V)]
    # 누적 거리를 저장할 변수
    distance = [INF] * V
    # 간선 정보 저장

    for i in range(N):
        for j in range(N-1):

            # 행, 열 간 이동 소비량 가중치로 저장
            if matrix[i][j+1] > matrix[i][j]:
                graph[i*N+j].append([matrix[i][j+1] - matrix[i][j]+1,i*N+j+1])
                graph[i * N + j + 1].append([1,i * N + j] )
            else:
                graph[i * N + j].append([1,i * N + j + 1])
                graph[i * N + j + 1].append([matrix[i][j] - matrix[i][j+1]+1,i * N + j])
            if matrix[j+1][i] > matrix[j][i]:
                graph[j*N+i].append([matrix[j+1][i] - matrix[j][i] +1,(j+1)*N+i])
                graph[(j+1)*N+i].append([1,j*N+i])
            else:
                graph[j * N + i].append([1,(j + 1) * N + i])
                graph[(j + 1) * N + i].append([matrix[j][i] - matrix[j+1][i] +1,j * N + i])
                # 2차원배열을 그래프로 바꾸기. 좌표들을 노드로 취급
                # 0~N-1까지의 노드를 가진 그래프로 변환.



    dijkstra(0)
    print(graph)