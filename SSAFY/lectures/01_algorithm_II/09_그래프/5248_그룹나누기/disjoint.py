# disjoint

def find_set(node):
    # parent 정보의 node번째에 기록된 값이 node가 아니면!
    # 자기 자신이 루트가 아니므로, 계속 해서 찾아나간다.
    if parent[node] != node:
        parent[node] = find_set(parent[node])
    return parent[node]

def union(x, y): # 두 집합을 합친다.
    # 루트 (조상이)가 자기 자신인지를 알아야한다.
    root_x = find_set(x)
    root_y = find_set(y)

    # 합집합을 하기 위해서 우리가 비교해야하느건
    # 서로 다른 조상을 가지고 있는 집단들이라면 합칠거다.
    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:   # 랭크가 같을떄는
            parent[root_y] = root_x
            rank[root_x] += 1



N = 5   # 0부터 4까지의 5개의 원소로 이루어진 집합
parent = list(range(N))     # 자기 자신을 부모로 초기화
print(parent)
rank = [1] * N   # 랭크를 1로 초기화

union(0, 1)
print(f'0과 1을 결합 {parent} {rank}')
print(find_set(0)) # 0
print(find_set(1)) # 0
union(1, 2)
print(f'1과 2를 결합 {parent} {rank}')
union(3, 4)
print(f'3과 4를 결합 {parent} {rank}')
union(2, 3)
print(f'2과 3을 결합 {parent} {rank}')