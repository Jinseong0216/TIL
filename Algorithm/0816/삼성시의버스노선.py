for x in range(1, int(input())+1):  # 테스트 케이스 수
    N = int(input())    # 버스 노선의 수
    routes = [list(map(int, input().split())) for _ in range(N)]    # 노선 정보(지나가는 위치)
    P = int(input())    # 버스 정류장의 수
    bus_stops = [int(input()) for _ in range(P)]    # 버스 정류장의 정보(위치)
    # ================ 초기 세팅 ================
    answer = []
    for bus_stop in bus_stops:  # 정류장마다 지가나는 노선 전부 확인 할 예정
        cnt = 0     # 지나가는 노선의 수
        for start, end in routes:   # 각 노선에 대해서 지나가는지 확인
            if start <= bus_stop <= end:    # 지나가는 노선이라면
                cnt += 1    # 개수 + 1
        answer.append(str(cnt))     # 지나가는 노선의 수를 answer에 추가(join 사용예정이라 str메서드 사용)

    print(f'#{x} {" ".join(answer)}')