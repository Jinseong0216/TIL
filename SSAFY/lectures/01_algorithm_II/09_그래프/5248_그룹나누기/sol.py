import sys
sys.stdin = open('input.txt')

# 자신이 속한 집단의 대표원소 (parent의 값)
def find_set(x):        # 부모가 자신이면 반환
    if x == parent[x]:
        return x
    else:               # 아니면 재귀
        return find_set(parent[x])

def union(x, y):
    x = find_set(x)
    y = find_set(y)

    # 랭크에 따른 부모 초기화
    if rank[x] >= rank[y]:
        parent[y] = x
    else:
        parent[x] = y

    # 랭킹 작업 완료 후, 동일 랭크에 대해서
    # 항상 x를 y의 부모로 잡고 있으므로, x의 랭크 1증가.
    if rank[x] == rank[y]:
        rank[x] += 1

T = int(input())

for tc in range(1, T+1):
    # N = 전체 사람 번호
    # M = 제출된 쪽지의 수
    N, M = map(int, input().split())
    # 간선 정보
    edge = list(map(int, input().split()))

    parent = list(range(N+1))   # 자신을 부모로 초기화
    rank = [0] * (N+1)          # 랭크를 0으로 초기화

    for i in range(M):      # 양쪽 노드 정보가 주어지므로
        x = edge[i*2]       # 왼쪽 노드
        y = edge[i*2+1]     # 오른쪽 노드
        union(x, y)

    # 평탄화
    for i in range(1, N+1):
        parent[i] = find_set(i)
    print(f'#{tc} {len(set(parent)) - 1}')
