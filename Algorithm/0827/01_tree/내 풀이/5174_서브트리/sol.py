import sys
sys.stdin = open('input.txt')

for T in range(1, int(input())+1):
    E, N = map(int, input().split())
    # 노드 정보를 담을 이중리스트 만들기!
    nodes = [[0, 0] for _ in range(E+2)]
    # 엣지 정보를 받아오기(전처리 단계)
    edge_data = list(map(int, input().split()))
    # 엣지 정보를 가공
    for i in range(E):
        P, C = edge_data[2*i], edge_data[2*i+1]
        # 우선적으로 왼쪽에 자식노드 지정
        if nodes[P][0] == 0:
            nodes[P][0] = C
        # 왼쪽에 자식 노드가 이미 지정이 되어있다면 오른쪽에 지정
        else:
            nodes[P][1] = C

    # 순회함수 정의
    def find_nodes(root):
        # 루트가 0인경우 탈출
        if root == 0: return 0
        # 현재 노드를 root로 하는 서브트리의 노드 개수는 자기자신 1 + 자식 노드의 개수
        return 1 + find_nodes(nodes[root][0]) + find_nodes(nodes[root][1])


    root = N
    ans = find_nodes(root)
    print(f'#{T}', ans)