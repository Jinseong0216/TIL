import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    # print(N, M)
    # for d in data:
    #     print(d)
    result = 0
    for x in range(N-M+1):
        for y in range(N-M+1):
            tmp = 0
            for i in range(x, x+M):
                for j in range(y, y+M):
                    if x+1 <= i <= x+M-2 and y+1 <= j <= y+M-2: continue
                    tmp += data[i][j]
            if result < tmp:
                result = tmp
    print(f'#{tc} {result}')
