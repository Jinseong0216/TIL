import sys
sys.stdin = open('input.txt')

import heapq

# q = []
# q.pop(0)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    q = []
    result = 0

    for n in map(int, input().split()):
        heapq.heappush(q, n)

    # print(q)
    while N > 1:  # 조상 노드 값 합산
        N //= 2
        result += q[N - 1]

    print(f'#{tc} {result}')