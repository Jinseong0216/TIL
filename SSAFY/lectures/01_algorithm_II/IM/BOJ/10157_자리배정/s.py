import sys
sys.stdin = open("input.txt")
# 공연장의 격자 크기
# 가로 : c, 세로 : r
c, r = map(int, input().split())

# 대기번호
k = int(input())

# 상우하좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 방문한곳과 콘서트장 생성
concert = [[0] * c for _ in range(r)]

# 좌석보다 대기번호가 더 긴경우
if c * r < k:
    print(0)

# 일반적인 경우
else:
    # 시작 index
    start_r, start_c = r-1, 0
    # 자리에 배치할 숫자
    cnt = 1
    i = 0
    # 시작할 때 방문
    concert[start_r][start_c] = cnt

    while cnt != k:
        # 공연장안에 있고 방문하지 않은 곳이면
        if 0 <= start_r + dr[i] < r and 0 <= start_c + dc[i] < c and not concert[start_r + dr[i]][start_c + dc[i]]:
            # 좌석번호 갱신
            cnt += 1

            # 현재위치 옮기기
            start_r += dr[i]
            start_c += dc[i]

            # 콘서트장에 좌석 배치
            concert[start_r][start_c] = cnt
        # 공연장 밖 or 방문한 곳
        else:
            i += 1
            i %= 4

    x = start_c + 1
    y = r - start_r
    print(x, y)
    answer = [x, y]