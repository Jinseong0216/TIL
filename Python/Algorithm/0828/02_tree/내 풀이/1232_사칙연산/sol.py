for T in range(1, 11):
    # 노드의 수
    N = int(input())
    # 해당 정점의 값, 왼쪽 자식 노드번호, 오른쪽 자식 노드번호
    edges = [[None, None, None] for _ in range(N+1)]
    for _ in range(N):
        # 입력을 잠시 저장
        temp = input().split()
        # 입력의 길이가 2인경우, edges[노드번호][0] = 노드의 값
        if len(temp) == 2: edges[int(temp[0])][0] = int(temp[1])
        # 입력의 길이가 4인경우, edges[노드번호] = [연산, 자식노드 번호1, 자식노드 번호2]
        else: edges[int(temp[0])] = [temp[1], int(temp[2]), int(temp[3])]

    # 연산을 진행하기 위한 함수 정의
    def cal(n, operator, m):
        if operator == '+': return n+m
        elif operator == '-': return n-m
        elif operator == '*': return n*m
        elif operator == '/': return n/m


    def fnct(root):
        # 부모노드의 값이 연산자이면
        if not str(edges[root][0]).isdecimal():
            # 자식1의 노드번호
            left = edges[root][1]
            # 자식2의 노드번호
            right = edges[root][2]
            # 자식1의 값이 연산자이면 재귀호출
            if not str(edges[left][0]).isdecimal(): fnct(left)
            # 자식2의 값이 연산자이면 재귀호출
            if not str(edges[right][0]).isdecimal(): fnct(right)
            # 모든 자식의 값이 숫자이면 위에서 정의한 함수를 통해서 연산을 진행함
            # 연산 결과를 해당 부모노드의 값으로 업데이트
            edges[root][0] = cal(edges[left][0], edges[root][0] , edges[right][0])

    # 루트번호
    root = 1
    # 정의한 함수 호출
    fnct(root)
    # 문제 형식에 맞게 출력
    print(f'#{T}', int(edges[root][0]))
