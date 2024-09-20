import sys
sys.stdin = open('input.txt')


def search(node):
    global count
    if node:    # 해당 노드가 존재 한다면 (0이 아니라면)
        count += 1      # 조사 시작했으니 count + 1
        search(tree[node][0])   # 왼쪽 노드에 대해서 조사
        search(tree[node][1])   # 오른쪽 노드에 대해서 조사


T = int(input())

for tc in range(1, T+1):
    # 간선의 개수 E, 탐색 시작 노드 번호 N
    E, N = map(int, input().split())
    # 부모, 자식 정보 E개
    arr = list(map(int, input().split()))
    # 노드 최대 번호 : 문제 상에는 E+1 로 되어 있으나,
    # 트리를 리스트 형태로 나타내게 되는 경우, E + 1 번 인덱스까지 표기하려면 +2 까지 필요.
    V = E + 2
    tree = [[0, 0] for _ in range(V)]   # 노드 개수 만큼 자식 정보 표기 트리
    # 0번 노드 없음,               LC, RC  각각 왼쪽 자식 노드 번호, 오른쪽 자식 노드 번호 표기
    # print(tree)     # [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

    # 자식 정보 갱신
    for i in range(E):  # E 개의 간선이란, (부모, 자식) 정보 한 세트가 E개 라는 의미
        '''
               0  1  2  3  4  5  6  7
        arr = [1, 2, 1, 3, 2, 4, 2, 5 ... ]
        부모 -> 0,    2,    4,    6,    8
        자식 ->    1,    3,    5,    7  ...
        i =     0     1     2
        부모 -> 0*2,  1*2,  2*2
        자식 ->  0*2+1, 1*2+1 ... 
        '''
        parent = arr[i*2]
        child = arr[i*2+1]
        if tree[parent][0] == 0:    # 아직 parent의 0번째 위치에 자식 정보를 기입 안했으면
            tree[parent][0] = child     # 자식 정보 기입
        else:                       # 이미 0번째에 기입 했다면,
            tree[parent][1] = child     # 남은 자리 1번째 자리에 자식 정보 기입

    # print(tree)       # 기입 완료된 자식 정보 확인 후,
    count = 0   # 시작 노드 기준으로 자식 노드가 얼마나 있는지 조사
    search(N)   # 조사 시작할 N번 노드부터 자식 요소들 조사 시작
    print(f'#{tc} {count}')     # 결과 출력
