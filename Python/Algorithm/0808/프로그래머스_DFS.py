# '''
# 출처: https://school.programmers.co.kr/learn/courses/30/lessons/43165
# '''

def solution(numbers, target):
    N = len(numbers)
    bound = [numbers[0]] + [0]*(N-2) + [numbers[-1]]
    for i in range(len(numbers)-2,-1,-1): bound[i] = numbers[i]+bound[i+1]
    answer = 0

    def cal(num,i):
        nonlocal answer
        if i == N-1 and num == target: answer += 1
        elif i < N-1:
            if (num + bound[i+1] >= target) and (num - bound[i+1] <= target):
                cal(num-numbers[i+1], i+1), cal(num+numbers[i+1], i+1)
    cal(numbers[0],0), cal(-1*numbers[0],0)
    return answer

