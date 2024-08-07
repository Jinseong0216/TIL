def solution(progresses, speeds):
    answer = []
    day = 0
    while day < 101:
        day, N = day +1, len(progresses)
        progresses = [progresses[i] + speeds[i] for i in range(N)]

        cnt = 0
        for i in range(N):  
            if progresses[i] < 100: 
                break
            cnt += 1
        if cnt: answer.append(cnt)
        progresses, speeds = progresses[cnt:], speeds[cnt:]

        if progresses == []: return answer