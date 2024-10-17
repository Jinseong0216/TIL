from collections import deque
N, M = map(int, input().split())
grid = [0]*101
for _ in range(N):
    prior, post = map(int, input().split())
    grid[prior] = post
for _ in range(M):
    prior, post = map(int, input().split())
    grid[prior] = post

dist = [-1]*101


def bfs():
    queue = deque([1])
    dist[1] = 0

    while queue:
        pin = queue.popleft()
        for num in range(1, 7):
            new_pin = pin+num
            if new_pin > 100: continue
            if grid[new_pin]: new_pin = grid[new_pin]
            if grid[new_pin] == 0:
                if dist[new_pin] == -1 or dist[new_pin] > dist[pin] + 1:
                    dist[new_pin] = dist[pin] + 1
                    queue.append(new_pin)


bfs()
print(dist[-1])
