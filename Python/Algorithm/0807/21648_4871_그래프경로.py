def DFS(s, e,V):
    visited = [0]*(V+1)
    stack =[]
    v = s
    while True:
        for w in adjL[v]:
            if w == e:
                return 1
            if visited[w] == 0:
                stack.append(w)
                v=w
                visited[w] = 1
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break
    return 0

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    adjL = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        adjL[u].append(v)

    S, G = map(int, input().split())
    ans = DFS(S, G, V)
    print(f'#{t} {ans}')