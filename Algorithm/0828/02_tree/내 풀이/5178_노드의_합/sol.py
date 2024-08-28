import sys
sys.stdin = open('input.txt')

# 테스트 케이스만큼 반복
for T in range(1, int(input()) + 1):
    # N = 노드의 수, M = 리프노드의 수, L = 타겟노드
    N, M, L = map(int, input().split())
    # edges[node] = [노드의 값, 자식노드 1, 자식노드 2]가 되도록 만들 것
    edges = [[None, None, None] for _ in range(N + 1)]
    # 리프노드의 값을 저장할 덱
    leaf_nodes = {}
    for _ in range(M):
        # node = 리프노드의 번호, value = 리프노드의 값
        node, value = map(int, input().split())
        # 딕셔너리에 리프노드의 값을 저장
        leaf_nodes[node] = value


    def fnct(root):
        # 자식노드 1의 노드번호 계산
        child = 2 * root
        # 자식을 가지는 노드라면
        if child <= N:
            # 자식노드의 값을 저장할 리스트
            wait_sum = []
            # 자식노드 1의 값이 아직 없다면, 재귀호출
            if not edges[root][1]: fnct(child)
            # 자식노드 1의 값을 리스트에 저장
            wait_sum.append(edges[child][0])
            # 자식노드 2를 가지는 노드라면
            if child + 1 <= N:
                # 자식노드 2의 값이 아직 없다면, 재귀호출
                if not edges[root][2]: fnct(child + 1)
                # 자식노드 2의 값을 리스트에 저장
                wait_sum.append(edges[child + 1][0])
            # 자식노드가 하나인 경우를 에러를 방지하기 위함
            wait_sum.append(0)
            # 자식노드의 합을 현재 노드의 값으로 업데이트
            edges[root][0] = sum(wait_sum)

        # 리프노드라면, 저장한 리프노드의 값을 찾아서 할당함
        else: edges[root][0] = leaf_nodes[root]
        # 만약 노드의 번호가 타겟 번호라면, 해당 노드의 값을 출력한다
        if root == L: print(f'#{T}', edges[root][0])


    root = 1
    fnct(root)