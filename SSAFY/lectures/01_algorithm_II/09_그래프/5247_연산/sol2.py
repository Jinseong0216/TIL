import sys
sys.stdin = open('input.txt')

def BFS():
    front = rear = -1
    visited[N] = 1          # 방문 기록
    rear += 1
    Q[rear] = N             # 큐에 시작 노드 인큐
    while front != rear:    # 큐가 비어있지 않으면
        front += 1
        now = Q[front]        # 다음 노드를 꺼내
        # 인접 노드번호 계산
        for i in [now + 1, now - 1, now * 2, now - 10]:
            if i == M:  # 찾는 노드인 경우 거리 리턴
                return visited[now]

            if i > 0 and i <= 1000000:  # 유효한 노드 번호이므로
                if visited[i] == 0:  # 아직 방문하지 않은 노드면
                    visited[i] = visited[now] + 1  # 거리를 기록하고
                    rear += 1
                    Q[rear] = i

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    '''
        최대 Q의 범위를 선정하기.
        이번 문제에서는 연산 방식에 +1 이 들어있으므로,
        0부터 100만까지 모든 경우가 Q에 삽입될 가능성이 있으므로, 최악의 경우 100만번 연산이 필요하다.
        따라서, 조사 대상을 삽입할 Q의 최대 크기는 100만이 된다.
    '''
    Q = [0]*(1000000)               # 최대 100만 까지만 연산 할 것이므로
    '''
        visited의 경우도 마찬가지로 0부터 100만까지 모든 경우에 대해 방문 할 수 도 있으므로
        대신, Q는 다음 조사 대상을 삽입할 위치이고,
        visited의 경우는...
        N이 1이었을때,
        +1 연산을 한 결과인 2와
        *2 연산을 한 결과인 2가
        
        어찌되었든 2라는 동일한 값을 가지게 되므로,
        동일한 값을 갖게되는 연산에 대해서는 다시 다음 조사 대상으로 삽입할 필요 없으므로 
        이를 체크하기 위해 사용한다.
    '''
    visited = [0] * 1000001         # 100만에 대해 이미 연산해 본 적이 있었다면, 다시 연산할 필요 없이...
    print(f'#{tc} {BFS()}')