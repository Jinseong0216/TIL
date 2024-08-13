def solution(priorities, location):
    cnt, answer, priorities_list = [0]*11, 0, []
    for i in range(len(priorities)):
        cnt[priorities[i]] += 1
        priorities_list.append([i, priorities[i]])

    while True:
        process = priorities_list.pop(0)
        if sum(cnt[process[1] + 1:]) == 0:
            cnt[process[1]], answer = cnt[process[1]]+1, answer+1
            if process[0] == location: break
        else: priorities_list.append(process)
    return answer
