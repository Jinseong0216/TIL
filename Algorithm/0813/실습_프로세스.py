def solution(priorities, location):
    cnt = [0]*11
    property_list = []
    for i in range(len(properties)):
        cnt[properties[i]] += 1
        property_list = []
    process = priorities.pop(0)
    if sum(cnt[process+1:]) == 0:
        cnt[process] -= 1
        answer += 1
    else:
    answer = 0
    return answer
