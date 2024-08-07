def DFS(start, end):
    v = start
    stack = [v]
    visited = [0]*(99+1)
#    visited[v] = 1
    while True:
        print(stack)
        if v == end: 
            return 1
        for w in adjL[v]:
            if visited[w] == 0:
                stack.append(w)
                visited[w] = 1
                v = w
                break
        else:
            if stack:
                v = stack.pop()
            else:
                return 0
result = []
for _ in range(10):
    tc, E = map(int, input().split())
    edges = list(map(int, input().split()))
    adjL = [[]*(99+1)]
    for i in range(E): adjL[edges[2*i]].append(edges[2*i+1])

    ans = DFS(0, 99)
    result.append(ans)
#    print(f'#{tc} {ans}')
print((result))
#    print(adjL)