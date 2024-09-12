T = int(input())    # 테스트 케이스의 수
for tc in range(1, T+1):
    N, K = map(int, input().split())    # N, K 입력값 받아오기
    seq = [0] + list(map(int, input().split()))     # 인덱스의 편의를 위해 0 padding

    idx = 1     # 미생물의 출발 위치 지정
    while idx <= N:     # 미생물의 출발 위치가 N보다 같거나 작은 경우까지 반복문
        dist = 0    # 이동할 수 있는 거리를 측정하기 위함
        for weight in range(K, 0, -1):  # 최대 이동거리는 K임. idx를 기준으로 거리가 K에서 1사이에 먹이가 존재하는지 체크하기 위함
            if idx+weight > N: continue     # idx+weight가 범위초과인 경우 제외
            if seq[idx+weight] == 1:    # idx+weight의 위치에 먹이가 있다면
                dist = weight   # 이동거리를 찾고 break
                break
        idx = idx + dist    # 이동거리내의 가장 먼 먹이 위치로 idx를 업데이트
        if dist == 0:   # 만약 이동거리내에 먹이가 없다면
            idx = idx + K   # 최대 이동거리로 idx를 업데이트하고 반복문을 멈춘다.
            break

    answer = min(N, idx)    # 도출된 최대 이동거리가 N보다 큰 경우 N으로 변경
    print(f'#{tc} {answer}')
