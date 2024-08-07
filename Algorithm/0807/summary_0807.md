## 08/07(수)

### 09:00 ~
- 깊이우선탐색

- 빠짐없이 검색 !! 조건 제하고
- 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시
- 깊이 우선 탐색을 반복해야 하므로 후입선출 구조의 스택 사용
- 두번째는 재귀를 사용

```
1
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
```

```
def DFS(s, V):      # s-시작, V-1번부터 정점인 마지막 정점(정점개수)
    visited = [0] * (V+1)    # 방문한 정점 표시
    stack = []
    print(f'#s {s}')
    visited[s] = 1  # 시작 정점 방문 표시
    v = s
    while True:
        for w in adjL[v]:   # v에 인접하고, 방문안한 w 가 있으면
            if visited[w] == 0:  # 아직 방문 안했으면
                stack.append(v)  # push(v) 현재 정점을 push하고
                v = w            # w에 방문
                print(v)
                visited[w] = 1     # w에 방문 표시
                break            # v부터 다시 탐색 for의 break
        else:                   # 남은 인접 정점이 없어서 break가 걸리지 않은 경우 for else
            if stack:           # 이전 갈림길을 스택에서 꺼내 Top 쓰면 if Top = -1로
                v = stack.pop()
            else:           # 남은 갈림길 없으면, 되돌아갈 곳이 없으면 탐색 종료
                break   # while 문의 break
```

```
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())    # V = 마지막 7   E = 8쌍
    adjL = [[] for _ in range(V+1)]     # V + 1
    arr = list(map(int, input().split()))
    # 두개씩 가져오는 작업
    for i in range(E):
        v1, v2 = arr[i*2], arr[i*2+1]   # 정점1, 정점2
        adjL[v1].append(v2)
        adjL[v2].append(v1)
    print(adjL)
    DFS(1, V)
```