import sys
sys.stdin = open('input.txt')

def findSet(x):
    if x == parent[x]:
        return x
    else:
        return findSet(parent[x])

def mst():
    cnt = 0 # 간선의 개수
    result = 0 # 전체 가중치의 합
    idx = 0 # 조사 대상

    # MST 구성하는 반복문
    while cnt < V: # 사이클 없는 트리의 간선의 개수는 V-1
        p1 = findSet(arr[idx][0])
        p2 = findSet(arr[idx][1])
        # 사이클이 형성되지 않을때
        if p1 != p2:
            # arr 은 가중치 기준으로 오름차순 정렬 하였으므로 일단 삽입
            result += arr[idx][2]   # idx 번째 정보의 n1 과 n2 사이의 간선잇기
            cnt += 1    # 간선 개수 하나 늘림
            parent[p2] = p1
        idx += 1
        # print(parent)
    return result


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]

    arr.sort(key=lambda x: x[2])
    parent = list(range(V+1))
    print(f'#{tc} {mst()}')