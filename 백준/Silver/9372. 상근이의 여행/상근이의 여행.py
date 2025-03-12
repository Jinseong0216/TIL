for T in range(int(input())):
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    parents = [i for i in range(N+1)]

    def find_set(x):
        if parents[x] == x:
            return x

        parents[x] = find_set(parents[x])  # 경로 압축
        return parents[x]

    def union(x, y):
        root_x = find_set(x)
        root_y = find_set(y)

        if root_x == root_y:
            return

        # 더 작은 루트노트에 합친다.
        if root_x < root_y:
            parents[root_y] = root_x
        else:
            parents[root_x] = root_y

    # MST의 간선수 N = 정점 수 - 1
    cnt = 0     # 선택한 edge의 수 (사용이유: N - 1 가 되면 신장트리 완성) - 시간 효율을 위해 사용


    for u, v in edges:
        # 출발점과 도착점이 같은 그룹에 속해있다면, 이미 연결된 친구들이다.
        # 다른 집합이라면
        if find_set(u) != find_set(v):  # 싸이클이 없다면
            cnt += 1
            union(u, v)
            if cnt == N - 1:  # MST 구성이 끝나면
                break

    print(cnt)