def solution(n):
    answer = 0
    
    def make_parenthesis(left_remained, used_left, used_right, step, bp):
        nonlocal answer

        if step == bp: answer +=1; return;
        if left_remained < 0 or used_left > n or used_right > n: return;
        make_parenthesis(left_remained+1, used_left+1, used_right, step+1, bp)
        make_parenthesis(left_remained-1, used_left, used_right+1, step+1, bp)
        return
    
    make_parenthesis(0, 0, 0, 0, 2*n+1)
    return answer//2
