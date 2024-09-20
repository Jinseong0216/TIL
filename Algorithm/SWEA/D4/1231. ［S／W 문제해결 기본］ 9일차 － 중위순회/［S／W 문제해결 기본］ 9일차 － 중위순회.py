for tc in range(1, 11):
    N = int(input())
    vertices_info = {}
    left = [0]*(N+1)
    right = [0]*(N+1)

    for _ in range(N):
        info = list(input().split())
        L = len(info)
        v = int(info[0])
        vertices_info[v] = info[1]
        if L == 2: continue
        left[v] = int(info[2])
        if L == 3: continue
        right[v] = int(info[3])


    def inorder(node):
        if node == 0: return

        inorder(left[node])
        print(vertices_info[node], end='')
        inorder(right[node])

    root = 1
    print(f'#{tc} ', end='')
    inorder(root)
    print()