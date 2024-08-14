# deque 써서 풀기 (복습문제)
from collections import deque

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    numbers = deque(input().split())

    cnt = 0
    while cnt < M:
        numbers.rotate(-1) # numbers.append(numbers.popleft())과 같음!!
        cnt += 1
    print(f'#{t}', numbers.popleft())
