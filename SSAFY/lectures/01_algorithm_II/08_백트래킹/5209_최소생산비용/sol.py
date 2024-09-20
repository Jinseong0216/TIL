import sys
sys.stdin = open('input.txt')


def search(now, acc):
    global result
    '''
        now : 현재 조사 대상 제품
        acc : 누적 생산 비용  
    '''

    if acc > result:    # 모든 제품을 조사하지는 않았으나, 누적값이 초과했다면,
        return          # 유망성 없음.

    if now == N:            # 모든 제품에 대해 조사를 마쳤다면
        if result > acc:    # 최솟값 비교
            result = acc    # 최솟값 갱신
        return
    else:
        for w in range(N):      # 모든 공장의 now 번째 제품 생산 비용을 누적 해 볼 수 있도록
            if not visited[w]:  # 아직 w 번째 공장에서 제품을 생산한 적이 없다면,
                visited[w] = 1  # 해당 공장에서 now 번째 제품을 생산할 것이라고 표기 후,
                search(now+1, acc + data[now][w])   # 다음 제품 조사 시작, 누적값 증가
                visited[w] = 0  # backtracking

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    result = 15*99
    visited = [0] * N
    search(0, 0)
    print(f'#{tc} {result}')