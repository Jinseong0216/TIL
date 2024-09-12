def DFS(start, end):
    v = start
    visited = [0]*(99+1)
    stack = []
    while True:
        if v == end:
            return 1

        for w in adjL[v]:
            if visited[w] == 0: # 방문 x인 곳이면
                stack.append(v) # 현 위치를 stack에 넣고
                visited[v] = 1 # v를 방문했다고 표시
                w = v
                break
        
        else:                    # 모든 인접 노드들이 방문한 노드들이면
            if stack:            # 뒤로 갈 곳이 있으면
                w = stack.pop()  # w를 바로 뒤의 점으로
            else:               # 뒤로 갈 곳이 없으면
                return 0
            
for t in range(10):
    tc, E = map(int, input().split())
    edges = list(map(int, input().split()))
    adjL = [[] for _ in range(99+1)]
    for i in range(E): adjL[edges[2*i]].append(edges[2*i+1])

    v = 0
    visited = [0]*(99+1)
    visited[v] = 1
    stack = []
    stack.append(v)
    while True:
        if v == 99:
            ans = 1
            break

        for w in adjL[v]:
            if visited[w] == 0:  # 방문 x인 곳이면
                v = w            # 위치를 w로 변경
                stack.append(v)  # w 위치를 stack에 넣고
                visited[v] = 1   # w를 방문했다고 표시
                break

        else:                    # 모든 인접 노드들이 방문한 노드들이면
            if stack:            # 뒤로 갈 곳이 있으면
                v = stack.pop()  # w를 바로 뒤의 점으로
            else:               # 뒤로 갈 곳이 없으면
                ans = 0
                break
    print(f'#{tc} {ans}')
