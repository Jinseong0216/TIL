weight = int(input())
result = []
a, b = [0, 0]
for _ in range(6):
    direction, distance = map(int, input().split())
    if direction == 1: a += distance
    if direction == 2: a -= distance
    if direction == 3: b -= distance
    if direction == 4: b += distance
    result.append([a, b])

A = B = float('-inf')
C = D = float('inf')
for position in result:
    A, B = max(A, position[0]), max(B, position[1])
    C, D = min(C, position[0]), min(D, position[1])

# 1. 중간 좌표 탐색

# 2. 빈 공간이 어떤 사분면에 있는지 찾기
