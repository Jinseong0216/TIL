import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    # 노드의 정보를 받아오기 위한 딕셔너리
    vertices_info = {}
    # 왼쪽 자식 노드의 정보를 담을 리스트
    left = [0]*(N+1)
    # 오른쪽 자식 노드의 정보를 담을 리스트
    right = [0]*(N+1)
    # 위의 리스트에서 0을 넣는 이유는, 순회 함수를 작성할 때
    # node == 0 인경우 탈출 조건을 지정하기 위함

    # 이진트리 구성하기
    for _ in range(N):
        info = list(input().split())
        L = len(info)
        v = int(info[0])
        vertices_info[v] = info[1]
        if L == 2: continue
        left[v] = int(info[2])
        if L == 3: continue
        right[v] = int(info[3])


    # 순회 함수 정의
    def inorder(node):
        # 탈출 조건
        if node == 0: return
        # 왼쪽 자식노드 먼저 탐색
        # 어짜피 자식노드가 0인경우, 바로 함수가 종료되니 상관없음
        # 왼쪽으로 갈수 있는 만큼 가보자!
        inorder(left[node])
        # 더이상 왼쪽으로 갈 수 없다면 해당 위치를 방문 한 것으로 고려함!
        print(vertices_info[node], end='')
        # 오른쪽으로 갈 수 있는 만큼 가보자!
        inorder(right[node])


    root = 1
    inorder(root)
    print()