def find_set(x):
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y: return

    if x < y:
        parents[y] = x
    else:
        parents[x] = y

# 노드의 개수, 간선의 개수를 입력받기
V, E = 7, 11
edge = [
    [0, 1, 32],
    [0, 2, 31],
    [0, 5, 60],
    [0, 6, 51],
    [1, 2, 21],
    [2, 4, 46],
    [2, 6, 25],
    [3, 4, 34],
    [3, 5, 18],
    [4, 5, 40],
    [4, 6, 51],
]

edge.sort(key=lambda x: x[2])       # 가중치 기준으로 정렬
parents = [i for i in range(V)]     # 부모 정보 초기화

cnt = 1         # 모든 노드 방문 처리 되었는지 확인
result = 0      # 누적값 갱신

for x, y, weight in edge:
    print(x, y, weight)
    # 부모가 일치하지 않다면
    if find_set(x) != find_set(y):
        cnt += 1            # 노드 집합
        union(x, y)
        print(x, y)         # 방문 순서 출력
        result += weight    # 값 누적
        if cnt == V:        # 모든 노드 처리 집합 완료시 종료.
            break
print(result)
