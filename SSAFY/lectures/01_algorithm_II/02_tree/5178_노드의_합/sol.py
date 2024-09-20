import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 노드 개수, 리프 노드의 수, 출력할 노드 번호
    N, M, L = map(int, input().split())

    # 완전 이진트리이므로 노드의 개수 만큼만 트리를 그리면 된다.
    # 단, 0번 노드는 사용하지 않음.
    tree = [0] * (N+1)

    for _ in range(M):      # M번에 걸쳐 리프 노드 번호와 자연수
        leaf, num = map(int, input().split())
        tree[leaf] = num    # 트리에 값 삽입

    # while N:   # 0번 노드가 되기 전까지 작업
    while N != L*2-1:   # L 의 직계 자식까지만 연산 하면 됨
        child = N
        parent = N//2   # 현재 노드의 부모 노드 번호
        tree[parent] += tree[child]     # 부모 노드 위치에 현재 노드 값 덧셈
        N -= 1          # 노드 번호를 한 칸씩 당기며 연산

    print(f'#{tc} {tree[L]}')

