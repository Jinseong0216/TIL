import sys
sys.stdin = open('input.txt')


def search(now, battery, acc):
    global result
    '''
        now : 현재 정류장 위치
        battery : 남은 배터리 잔량
        acc : 누적 충전 횟수
   '''
    if acc > result:    # 아직 종점에 도달하지 않았으나, 최소 충전량 보다 많다면
        return          # 유망성 없음.

    if now == N-1:          # 최종 목적지에 도착했다면,
        if result > acc:    # 최솟값 비교
            result = acc    # 최솟값 갱신
        return              # 조사 종료
    else:
        if battery:                                     # 배터리가 남았으면
            search(now + 1, battery - 1, acc)           # 일단 충전 없이 가 보거나
        search(now + 1, station[now] - 1, acc + 1)      # 충전 하고 이동



T = int(input())

for tc in range(1, T+1):
    N, *station = map(int, input().split())
    result = N  # 충분히 많은 충전 횟수 : 모든 정류장에서 충전을 했다면
    search(0, station[0], 0)
    print(f'#{tc} {result}')