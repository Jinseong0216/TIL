def make_parents(num):
    return [n for n in range(num+1)] # 시작 노드가 1임을 고려

def find_parents(node, parents):
    if parents[node] == node: return node
    return find_parents(parents[node], parents)

def union(node_u, node_v, parents):
    if find_parents(node_u, parents) == find_parents(node_v, parents): 
        return
    elif find_parents(node_u, parents) > find_parents(node_v, parents):
        parents[find_parents(node_u, parents)] = find_parents(node_v, parents)
        return
    else:
        parents[find_parents(node_v, parents)] = find_parents(node_u, parents)
        return

N, M = int(input()), int(input())
parents = make_parents(N)
edges = [list(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x: x[2])

total, cnt = 0, 0
for u, v, weight in edges:
    if cnt >= N-1: break
    if find_parents(u, parents) == find_parents(v, parents): continue
    union(u, v, parents)
    total, cnt = total+weight, cnt+1

print(total)