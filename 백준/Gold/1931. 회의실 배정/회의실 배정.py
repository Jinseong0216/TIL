def max_meetings(N, meetings):
    # 종료 시간 기준으로 정렬, 종료 시간이 같으면 시작 시간 기준으로 정렬
    meetings.sort(key=lambda x: (x[1], x[0]))

    count = 0  # 최대 회의 개수
    last_end_time = 0  # 마지막으로 선택된 회의의 종료 시간

    for start, end in meetings:
        if start >= last_end_time:  # 현재 회의가 겹치지 않는 경우
            count += 1
            last_end_time = end  # 현재 회의의 종료 시간을 갱신

    return count

# 입력 처리
N = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(N)]

# 최대 회의 개수 계산
result = max_meetings(N, meetings)
print(result)
