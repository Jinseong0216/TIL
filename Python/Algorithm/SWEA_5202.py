# 화물도크 5202 SWEA
def function(time, W):
    global ans
    # 24시가 된 경우, 업데이트 후 리턴
    if time == 24: ans = max(ans, W); return;
    # 해당 시간에 작업을 안한다고 선택한 것
    function(time + 1, W)
    # 해당 시간에 작업을 한다고 선택한 것
    for i in range(len(info[time])):
        # 가능한 작업을 골라서, 해당 작업이 끝나는 시간대로 이동 후 재귀호출
        function(info[time][i], W + 1)

# 테스트케이스의 수
for T in range(1, int(input())+1):
    # 총 작업량
    N = int(input())
    # 작업의 끝을 저장하기 위함
    info = [[] for _ in range(24)]
    for _ in range(N):
        # 시작, 끝
        s, e = map(int, input().split())
        # 시작시간과 같은 위치에 종료시점을 넣기
        info[s].append(e)
    ans = 0

    function(0, 0)
    print(f'#{T}', ans)