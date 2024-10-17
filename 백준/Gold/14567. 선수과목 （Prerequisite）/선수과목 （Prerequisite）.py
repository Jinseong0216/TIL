from collections import deque
import sys

input = sys.stdin.readline


def search():
    queue = deque([i for i in range(N) if in_degree[i] == 0])
    completed, semester = 0, 0

    while queue:
        semester += 1
        for _ in range(len(queue)):
            current = queue.popleft()
            ans[current] = semester
            completed += 1

            for post in graph[current]:
                in_degree[post] -= 1
                if in_degree[post] == 0:
                    queue.append(post)


N, M = map(int, input().split())
graph = [[] for _ in range(N)]
in_degree = [0]*N

for _ in range(M):
    prior, post = map(int, input().split())
    prior, post = prior-1, post-1
    graph[prior].append(post)
    in_degree[post] += 1

ans = [0]*N
search()
print(*ans)
