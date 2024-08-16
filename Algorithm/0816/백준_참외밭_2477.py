weight = int(input())
position_list = []
a, b = [0, 0]
for _ in range(6):
    direction, distance = map(int, input().split())
    if direction == 1: a += distance
    if direction == 2: a -= distance
    if direction == 3: b -= distance
    if direction == 4: b += distance
    position_list.append([a, b])

A = B = float('-inf')
C = D = float('inf')
for position in position_list:
    A, B = max(A, position[0]), max(B, position[1])
    C, D = min(C, position[0]), min(D, position[1])

center = 0
# 1. 중간 좌표 탐색
for x, y in position_list:
    if C < x < A and D < y < B: center = [x, y]
# 2. 빈 공간이 어떤 사분면에 있는지 찾기
a = b = 0
full_position_list = [[C, D], [C, B], [A, D], [A, B]]
for position in full_position_list:
    if position not in position_list: a, b = position

answer = weight*(abs((B-D)*(A-C)) - abs((a-center[0])*(b-center[1])))
print(answer)
