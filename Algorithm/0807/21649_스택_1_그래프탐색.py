def DFS(s, V):
    visited = [0]*(V+1)
    visited[1] = 1
    stack =[1]
    route = [str(s)]
    v = s
    while len(route) < E:
        for w in adjL[v]:
            if visited[w] == 0:
                if str(w) not in route: route.append(str(w))
                stack.append(w)
                v=w
                visited[w] = 1
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break
    return route


V, E = map(int, input().split())
arr = list(map(int, input().split()))    
adjL = [[] for _ in range(V+1)]    

for i in range(E):
    u, v = arr[2*i], arr[2*i + 1]
    adjL[u].append(v)
    adjL[v].append(u)

for i in range(1, V+1):
    for j in range(len(adjL[i])-1, 0, -1):
        for k in range(j-1):
            if adjL[i][k] > adjL[i][k+1]:
                adjL[i][k], adjL[i][k+1] = adjL[i][k+1], adjL[i][k]
ans = '-'.join(DFS(1, V))
print(f'#1 {ans}')