N, M = map(int, input().split())

arr = list(range(1, N+1))
visited = [True] + [False]*N
seq = []
def dfs(length = 0):
    if length == M: print(" ".join(seq)); return

    for num in arr:
        if visited[num]: continue
        visited[num] = True
        seq.append(str(num))
        dfs(length+1)
        seq.pop()
        visited[num] = False
    return

dfs()