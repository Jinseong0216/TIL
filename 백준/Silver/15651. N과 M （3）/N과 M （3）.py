N, M = map(int, input().split())

arr = list(range(1, N+1))
seq = []
def dfs(length = 0):
    if length == M: print(" ".join(seq)); return

    for num in arr:
        seq.append(str(num))
        dfs(length+1)
        seq.pop()
    return

dfs()